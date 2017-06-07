from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core import serializers
from home.models import *
from django.db.models import F
from home.forms import *
import json
import random
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import Group
import sys



def index(request):
	project_list = Project.objects.filter(publish=True).filter(Q(status_id=1) | Q(status_id=2)).order_by("-fiscalyear")[:10]
	year_list = Ripples.objects.all().distinct('year').order_by('-year').values('year')
	ripple_list = serializers.serialize('json', Ripples.objects.all().order_by('-year'))
	ripple_article = serializers.serialize('json', Ripplesarticle.objects.all())
	return render(request, 'home/index.html', {'projects': project_list, 'years': year_list, 'ripples': ripple_list, 'articles': ripple_article})

def sitemap(request):
	return render(request, 'home/sitemap.html')

def gen_key():
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
	key = ''
	for x in range(50):
		i = random.randrange(0, len(alphabet))
		key = key+alphabet[i]
	return key

def send_email_confirmation(request, email):
	subscriber = RipplesSubscribers.objects.get(email=email)

	key = subscriber.confirmation_key

	to = [subscriber.email,]
	frm = 'infotech@grmw.org'
	subj = "Email Verification"
	verify_href = "http://"+str(get_current_site(request))+"/confirm_subscriber/"+str(email)+"/"+str(key)+"/"
	unsubscribe_href = "http://"+str(get_current_site(request))+"/unsubscribe/"+str(email)+"/"+str(key)+"/"

	context = {
		'verify_href': verify_href,
		'unsubscribe_href': unsubscribe_href,
	}

	content = get_template('home/email_subscriber_template.html').render(Context(context))

	send_mail(subj, "PLAIN TEXT", frm, to, fail_silently=False, html_message=content)

def subscribe(request):
	payload = {
		'success': False,
		'message': 'An error occurred while processing your request.',
		'data': {'error': 'POST ERROR - request.method does not contain POST.'},
	}
	if request.method == 'POST':
		email = request.POST['email']
		form = add_subscriber(request.POST or None)
		if form.is_valid():
			#Save the user's email to the database with unique key
			form = form.save(commit=False)
			form.confirmation_key = gen_key()
			form.email = email
			form.save()

			#Send confirmation email to user
			send_email_confirmation(request, email)

			payload = {
				'success': True, 
				'message': 'An email has been sent to the supplied address, please click the link in the email to confirm your email address. Please note: if you do not complete this step, you will NOT be able to receive electronic copies of our Ripples Newsletter.',
				'data': {},
			}
			
		else:
			payload = {
				'success': False,
				'message': 'An error occurred while processing your resquest.',
				'data': {'error': form.errors},
			}

	return HttpResponse(json.dumps(payload), content_type='application/json')

def confirm_subscriber(request, email, conf_key):
	response = render(request, 'home/index.html')
	context = {}
	subscriber = RipplesSubscribers.objects.get(email=email)
	if subscriber:
		form = add_subscriber(instance=subscriber)
		if form:
			if(conf_key == subscriber.confirmation_key):
				form = form.save(commit=False)
				form.confirmed = True
				form.save()
				response = render(request, 'home/email_confirm_complete.html')
			else:
				context['error'] = "[ERROR: The provided confirmation key does not match our records]"
				response = render(request, 'home/email_confirm_error.html', context)
		else:
			context['error'] = "We could not find the listed subscriber, please contact infotech@grmw.org and report the issue."
			response = render(request, 'home/email_confirm_error.html', context)
	else:
		context['error'] = "That subscriber does not exist in our database"
		response = render(request, 'home/email_confirm_error.html', context)
	return response

def unsubscribe(request, email, conf_key):
	response = render(request, 'home/index.html')
	context = {}
	subscriber = RipplesSubscribers.objects.get(email=email)
	if subscriber:
		form = add_subscriber(instance=subscriber)
		if form:
			if(conf_key == subscriber.confirmation_key):
				#delete subscriber from database
				subscriber.delete()
				response = render(request, 'home/email_unsubscribe.html')
			else:
				context['error'] = "[ERROR: The provided confirmation key does not match our records]"
				response = render(request, 'home/email_confirm_error.html', context)
		else:
			context['error'] = "We could not find the listed subscriber, please contact infotech@grmw.org and report the issue."
			response = render(request, 'home/email_confirm_error.html', context)
	else:
		context['error'] = "That subscriber does not exist in our database"
		response = render(request, 'home/email_confirm_error.html', context)
	return response

def ripples_dashboard(request):
	response = HttpResponseRedirect("/")
	#make sure that we are the admin before we show this page
	is_admin = False
	group = Group.objects.get(name="Site Admin")
	if group in request.user.groups.all():
		is_admin = True

	if is_admin == True:
		ripples = Ripples.objects.all().order_by("-year", "-edition_id")
		context = {
			'ripples_objects': ripples,
		}
		response = render(request, "home/ripples-admin.html", context)
	else:
		response = HttpResponseRedirect("/")


	return response

def send_newsletter(request):
	response = HttpResponseRedirect("/")
	is_admin = False
	group = Group.objects.get(name="Site Admin")
	if group in request.user.groups.all():
		is_admin = True

	if is_admin == True: 
		if request.method == "POST":
			#get all ripples
			ripple_id = request.POST.get('id_ripple')
			ripples = Ripples.objects.all().order_by("-year", "-edition_id")
			ripple_to_send = ripples.filter(pk=ripple_id)[0]

			#build context and render the template with context
			context = {
				'content': request.POST.get('id_content')
			}
			ctxt={
				'message': 'Ripples Newsletter Sent',
				'ripples_objects': ripples,
			}

			#get all subscribers
			subscribers=[]
			recipients = RipplesSubscribers.objects.all().filter(confirmed=True)
			for recipient in recipients:
				subscribers.append(recipient.email)
				context['href_unsubscribe'] = "http://"+str(get_current_site(request))+"/unsubscribe/"+str(recipient.email)+"/"+str(recipient.confirmation_key)+"/"
				content = get_template('home/email_newsletter_template.html').render(Context(context)) 
				try:
					#setup and send email
					message = EmailMessage(request.POST.get('id_subject'), content, "infotech@grmw.org", [recipient.email,])
					message.attach_file(str(ripple_to_send.file))
					message.content_subtype = "html"
					message.send()
				except:
					ctxt['message'] = 'An error occurred - '+str(sys.exc_info()[0])

			response = render(request, "home/ripples-admin.html", ctxt)
	return response