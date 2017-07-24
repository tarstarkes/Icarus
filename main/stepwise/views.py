from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.urlresolvers import reverse
import user_login
from stepwise.forms import *
from stepwise.models import *
from random import randint
from weasyprint import HTML, CSS
from django.template.loader import get_template
from django.template import RequestContext
from django.conf import settings
from django.core.files import File
from django.contrib.auth.models import Group
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.mail import send_mail
import os
import shutil

def index(request):
	"""
	if request.user.is_authenticated:
		renderedTemplate = render(request, 'stepwise/index.html')
	else:
		renderedTemplate = render(request, 'user_login/login.html')"""
	renderedTemplate = render(request, 'stepwise/index.html')
	return renderedTemplate

def stepwise_portal(request):
	if request.user.is_authenticated:
		processes = Process.objects.all().filter(user_id=request.user.id)
		context = {
			'projects': processes
		}
		response = render(request, 'stepwise/stepwise_portal.html', context)
	else:
		err = "You must be logged in to enter stepwise, if you don't have a login, you can register by clicking the 'Register' button below."
		redirect = '/stepwise/stepwise_portal/'
		response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	return response

def stepwise_prospectus_clean_model(request, step):
	if request.user.is_authenticated:
		request.session['model_id'] = None
		#prospectus model
		data = {
			'title': 'Project '+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9)),
		}
		form = prospectus_step_1(data)
		if form.is_valid():
			model = form.save(commit=False) #allows us to get the instance of the model for setting current_step
			model.current_step = 1
			model = form.save()

			data = {
				'prospectus_id': Prospectus.objects.get(pk=model.id).id,
				'user_id': User.objects.get(pk=request.user.id).id,
				'current_step': 1,
				'percent_done': 0,
				'overall_status_id': Overall_status.objects.get(pk=1).id,
			}
			#shell model for prospectus
			PF = process_form(data)
			if PF.is_valid():
				PF.save()
			else:
				print(PF.errors)

			request.session['model_id'] = model.id
		response = HttpResponseRedirect(reverse('stepwise_prospectus', args=[1]))
	else:
		err = "You must be logged in to access stepwise, if you don't have a login, you can register by clicking the 'Register' button below."
		redirect = '/stepwise/stepwise_portal/'
		response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	return response

def stepwise_prospectus(request, step):
	if request.user.is_authenticated:
		if step == "1":
			#step 1 has it's own function because this is the instance in which we
			#first save the model
			response = stepwise_prospectus_step_1(request)
		elif step == "2":
			response = stepwise_prospectus_step(request, prospectus_step_2, step)
		elif step == "3":
			#step 3 has its own step because we must allow an option to add a 
			#landowner which is a whole step in and of itself
			response = stepwise_prospectus_step_3(request)
		elif step == "4":
			response = stepwise_prospectus_step(request, prospectus_step_4, step)
		elif step == "add_landowner":
			response = stepwise_prospectus_add_landowner(request)
		elif step == "5":
			response = stepwise_prospectus_step(request, prospectus_step_5, step)
		elif step == "6":
			response = stepwise_prospectus_step(request, prospectus_step_6, step)
		elif step == "7":
			response = stepwise_prospectus_step(request, prospectus_step_7, step)
		elif step == "8":
			response = stepwise_prospectus_step(request, prospectus_step_8, step)
		elif step == "9":
			response = stepwise_prospectus_step(request, prospectus_step_9, step)
		elif step == "10":
			response = stepwise_prospectus_step(request, prospectus_step_10, step)
		elif step == "11":
			response = stepwise_prospectus_step(request, prospectus_step_11, step)
		elif step == "12":
			response = stepwise_prospectus_step(request, prospectus_step_12, step)
		elif step == "13":
			#step 13 needs its own step because the form may be done by this point in
			#the process and we need to redirect to a different page if so. 
			response = stepwise_prospectus_step_13(request)
		elif step == "14":
			response = stepwise_prospectus_step(request, prospectus_step_14, step)
		elif step == "15":
			response = stepwise_prospectus_step_15(request)

	else:
		err = "You must be logged in to access stepwise, if you don't have a login, you can register by clicking the 'Register' button below."
		redirect = '/stepwise/stepwise_portal/'
		response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	return response

def stepwise_prospectus_step_1(request):
	#Grab form #1 if we have simply been redirected to this page
	form = prospectus_step_1()
	context = {
		'form': form,
		'current_step': 1, 
		'submit': "Save & Continue >>", 
		'action': "/1/",
	}
	if request.session['model_id'] != None:
		form = prospectus_step_1(instance=Prospectus.objects.get(pk=request.session['model_id']))
		context['form'] = form
		project = Process.objects.all().filter(prospectus_id=request.session['model_id'])[0]
		context['project'] = project
	response = render(request, 'stepwise/stepwise_prospectus_form.html', context)
	if request.method == 'POST':
		processedForm = prospectus_step_1(request.POST or None)
		if processedForm.is_valid():
			if request.session['model_id'] != None:
				model_id = request.session['model_id']
				model = Prospectus.objects.get(pk=model_id)
				processedForm = prospectus_step_1(request.POST or None, instance=model)
				model = processedForm.save(commit=False) #allows us to get the instance of the model for setting current_step
				model.current_step = 1
				model = processedForm.save()
				#go to the next step
				response = HttpResponseRedirect(reverse('stepwise_prospectus', args=[2]))
		else:
			context['form'] = processedForm
			response = render(request, 'stepwise/stepwise_prospectus_form.html', context)
	return response

def stepwise_prospectus_step_3(request):
	form = prospectus_step_3()
	model_id = request.session['model_id']
	landowners = Landowner.objects.all().filter(prospectus_id=model_id)
	context = {
		'form': form, 
		'current_step': 3, 
		'submit': "Save & Continue >>", 
		'action': "/3/",
		'landowners': landowners,
	}
	if request.session['model_id'] != None:
		form = prospectus_step_3(instance=Prospectus.objects.get(pk=request.session['model_id']))
		context['form'] = form
		project = Process.objects.all().filter(prospectus_id=request.session['model_id'])[0]
		context['project'] = project
	response = render(request, 'stepwise/stepwise_prospectus_form.html', context)
	if request.method == 'POST':
		model = Prospectus.objects.get(pk=model_id)
		processedForm = prospectus_step_3(request.POST or None, instance=model)
		if processedForm.is_valid():
			model = processedForm.save(commit=False) #allows us to get the instance of the model for setting current_step
			model.current_step = 3
			model = processedForm.save()
			response = HttpResponseRedirect(reverse('stepwise_prospectus', args=[4]))
		else:
			context['form'] = processedForm
			response = render(request, 'stepwise/stepwise_prospectus_form.html', context)
	return response

def stepwise_prospectus_add_landowner(request):
	form = prospectus_add_landowner()
	context = {
		'form': form, 
		'current_step': 3, 
		'submit': "Save & Continue >>", 
		'action': "/add_landowner/",
	}
	if request.session['model_id'] != None:
		form = prospectus_add_landowner(instance=Prospectus.objects.get(pk=request.session['model_id']))
		context['form'] = form
		project = Process.objects.all().filter(prospectus_id=request.session['model_id'])[0]
		context['project'] = project
	response = render(request, 'stepwise/stepwise_add_landowner.html', context)
	if request.method == 'POST':
		model_id = request.session['model_id']
		processedForm = prospectus_add_landowner(request.POST or None)
		if processedForm.is_valid():
			model = processedForm.save(commit=False) #allows us to get the instance of the model for setting current_step
			model.prospectus_id = Prospectus.objects.get(pk=model_id)
			model.user_id = User.objects.get(pk=request.user.id)
			model = processedForm.save()
			response = HttpResponseRedirect(reverse('stepwise_prospectus', args=[3]))
		else:
			context['form'] = processedForm
			response = render(request, 'stepwise/stepwise_add_landowner.html', context)
	return response

def stepwise_delete_landowner(request, landowner_id):
	if request.user.is_authenticated:
		landowner = Landowner.objects.get(pk=landowner_id)
		if landowner.user_id.id == request.user.id:
			landowner.delete()
			response = HttpResponseRedirect(reverse('stepwise_prospectus', args=[3]))
		else:
			err = "You must be logged in to that account to make changes, please log in with the correct credentials and try again."
			redirect = '/stepwise/stepwise_portal/'
			response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	else:
		err = "You must be logged in to access stepwise, if you don't have a login, you can register by clicking the 'Register' button below."
		redirect = '/stepwise/stepwise_portal/'
		response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	return response

def stepwise_prospectus_step(request, prospectus_form, step):
	model_id = request.session['model_id']
	form = prospectus_form()
	context = {
		'form': form, 
		'current_step': step, 
		'submit': "Save & Continue >>", 
		'action': "/"+step+"/",
	}
	if model_id != None:
		form = prospectus_form(instance=Prospectus.objects.get(pk=model_id))
		context['form'] = form
		project = Process.objects.all().filter(prospectus_id=request.session['model_id'])[0]
		context['project'] = project
	response = render(request, 'stepwise/stepwise_prospectus_form.html', context)
	if request.method == 'POST':
		#get the working instance of the model
		model = Prospectus.objects.get(pk=model_id)
		processedForm = prospectus_form(request.POST or None, instance=model)
		if processedForm.is_valid():
			model = processedForm.save(commit=False) #allows us to get the instance of the model for setting current_step
			model.current_step = step
			model = processedForm.save()
			#go to the next step
			response = HttpResponseRedirect(reverse('stepwise_prospectus', args=[(int(step)+1)]))
		else:
			context['form'] = processedForm
			response = render(request, 'stepwise/stepwise_prospectus_form.html', context)
	return response

def stepwise_prospectus_step_13(request):
	form = prospectus_step_13()
	context = {
		'form': form, 
		'current_step': 13, 
		'submit': "Save & Continue >>", 
		'action': "/13/",
	}
	if request.session['model_id'] != None:
		form = prospectus_step_13(instance=Prospectus.objects.get(pk=request.session['model_id']))
		context['form'] = form
		project = Process.objects.all().filter(prospectus_id=request.session['model_id'])[0]
		context['project'] = project
	model_id = request.session['model_id']
	response = render(request, 'stepwise/stepwise_prospectus_form.html', context)
	if request.method == 'POST':
		#get the working instance of the model
		model = Prospectus.objects.get(pk=model_id)
		processedForm = prospectus_step_13(request.POST or None, instance=model)
		if processedForm.is_valid():
			model = processedForm.save(commit=False) #allows us to get the instance of the model for setting current_step
			model.current_step = 13
			model = processedForm.save()
			if(request.POST['grmw_design_funds'] == "True"):
				#go to the next step
				response = HttpResponseRedirect(reverse('stepwise_prospectus', args=[14]))
			elif(request.POST['grmw_design_funds'] == "False"):
				model.complete = True
				model = processedForm.save()
				request.session['model_id'] = None
				response = HttpResponseRedirect(reverse('stepwise_portal'))
			else:
				#should not happen unless someone is messing with the forms
				response = HttpResponseRedirect(reverse('stepwise_prospectus', args=[13]))
		else:
			context['form'] = processedForm
			response = render(request, 'stepwise/stepwise_prospectus_form.html', context)
	return response

def stepwise_prospectus_step_15(request):
	form = prospectus_step_15()
	context = {
		'form': form, 
		'current_step': 15, 
		'submit': "Save & Finish", 
		'action': "/15/",
	}
	if request.session['model_id'] != None:
		form = prospectus_step_15(instance=Prospectus.objects.get(pk=request.session['model_id']))
		context['form'] = form
		project = Process.objects.all().filter(prospectus_id=request.session['model_id'])[0]
		context['project'] = project	
	model_id = request.session['model_id']
	response = render(request, 'stepwise/stepwise_prospectus_form.html', context)
	if request.method == 'POST':
		#get the working instance of the model
		model = Prospectus.objects.get(pk=model_id)
		processedForm = prospectus_step_15(request.POST or None, instance=model)
		if processedForm.is_valid():
			model = processedForm.save(commit=False) #allows us to get the instance of the model for setting current_step
			model.current_step = 15
			model.complete = True
			model = processedForm.save()
			request.session['model_id'] = None
			response = HttpResponseRedirect(reverse('stepwise_portal'))
		else:
			context['form'] = processedForm
			response = render(request, 'stepwise/stepwise_prospectus_form.html', context)
	return response

def stepwise_detail(request, process_id):
	if request.user.is_authenticated():
		#get the process associated with the key provided
		project = Process.objects.all().filter(pk=process_id)[0]
		prospectus = Prospectus.objects.all().filter(pk=project.prospectus_id.id)[0]
		if prospectus.file == '' or prospectus.file == None:
			prospectus = None

		comments = Comment.objects.all().filter(process_id=process_id).order_by('date_created')
		drafts = Draft.objects.all().filter(process_id=process_id)
		comment_form = stepwise_comment_form()
		#check to make sure the logged in user matches the user on file for that process
		if request.user.id == project.user_id.id:
			context = {
				'project': project,
				'prospectus': prospectus,
				'comment_form': comment_form,
				'comments': comments,
				'draft_files': drafts,
			}
			response = render(request, 'stepwise/stepwise_project_detail.html', context)
		else:
			err = "You do not have the proper credentials to view this requested page, please login to the associated account and try again."
			redirect = '/stepwise/stepwise_detail/'+str(process_id)+'/'
			response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	else:
		err = "You must be logged in to access stepwise, if you don't have a login, you can register by clicking the 'Register' button below."
		redirect = '/stepwise/stepwise_detail/'+str(process_id)+'/'
		response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	return response

def stepwise_edit_prospectus(request, process_id):
	if request.user.is_authenticated():
		#get the process associated with the key provided
		project = Process.objects.all().filter(pk=process_id)[0]
		#check to make sure the logged in user matches the user on file for that process
		if request.user.id == project.user_id.id:
			request.session['model_id'] = project.prospectus_id.id
			step = project.prospectus_id.current_step
			response = HttpResponseRedirect(reverse('stepwise_prospectus', args=[step]))
		else:
			err = "You do not have the proper credentials to view this requested page, please login to the associated account and try again."
			redirect = '/stepwise/stepwise_detail/'+str(process_id)+'/'
			response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	else:
		err = "You must be logged in to access stepwise, if you don't have a login, you can register by clicking the 'Register' button below."
		redirect = '/stepwise/stepwise_detail/'+str(process_id)+'/'
		response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	return response

def stepwise_generate_prospectus(request, process_id):
	if request.user.is_authenticated():
		project = Process.objects.all().filter(pk=process_id)[0]

		if request.user.id == project.user_id.id:
			#generate the document
			landowners = Landowner.objects.all().filter(prospectus_id=project.prospectus_id.id)
			prospectus = Prospectus.objects.all().filter(pk=project.prospectus_id.id)[0]
			activities = prospectus.restoration_activities.all().order_by('activity_number')
			permits = prospectus.permits_consultations.all()
			all_permits = Permits_consults.objects.all()
			workTypes = prospectus.work_type.all()
			specialties = prospectus.work_specialties.all()

			context = {
				'project':project,
				'landowners': landowners,
				'activities': activities,
				'permits': permits,
				'all_permits': all_permits,
				'workTypes': workTypes,
				'specialties': specialties,
			}

			template = get_template('stepwise/stepwise_prospectus_template.html')
			rendered_html = template.render(RequestContext(request, context)).encode(encoding="UTF-8")
			pdf_file = HTML(string=rendered_html, base_url=request.build_absolute_uri()).write_pdf()
			
			#final_path = str('/static/documents/stepwise/prospectus/'+str(process_id)+'/prospectus'+str(process_id)+'.pdf')

			prospectus_model = Prospectus.objects.get(pk=project.prospectus_id.id)
			prospectus_model.file = SimpleUploadedFile('prospectus'+str(process_id)+'.pdf', pdf_file, content_type='application/pdf')
			prospectus_model.save()

			PFModel = Process.objects.get(pk=process_id)
			PFModel.percent_done = 15
			PFModel.current_step = 2
			PFModel.save()

			message = request.user.first_name+' '+request.user.last_name+' has generated a new prospectus for '+project.prospectus_id.title+'. Please login to GRMW.org to review it.'
			send_mail(
				'Prospectus Ready for Review',
				message,
				'infotech@grmw.org',
				#change this to projects@grmw.org for production server
				['projects@grmw.org'],
				fail_silently=False,
			)

			#redirect to stepwise process page
			response = HttpResponseRedirect(reverse('stepwise_detail', args=[process_id]))
		else:
			err = "You do not have the proper credentials to view this requested page, please login to the associated account and try again."
			redirect = '/stepwise/stepwise_detail/'+str(process_id)+'/'
			response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)			
	else:
		err = "You must be logged in to access stepwise, if you don't have a login, you can register by clicking the 'Register' button below."
		redirect = '/stepwise/stepwise_detail/'+str(process_id)+'/'
		response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	return response

def stepwise_comment(request, process_id):
	redir = "/stepwise/stepwise_detail/"+str(process_id)+"/"
	owner_id = Process.objects.filter(pk=process_id)[0].user_id.id
	response = stepwise_auth_user_ownership(request, owner_id, redir)
	if response == True:
		project = Process.objects.all().filter(pk=process_id)[0]
		if request.method == "POST":
			project = Process.objects.all().filter(pk=process_id)[0]
			documents = Prospectus.objects.all().filter(pk=project.prospectus_id.id)
			comments = Comment.objects.all().filter(process_id=process_id).order_by('date_created')
			drafts = Draft.objects.all().filter(process_id=process_id)
			form = stepwise_comment_form(request.POST or None, request.FILES or None)
			context = {
				'project': project,
				'documents': documents,
				'comment_form': form,
				'comments': comments,
				'draft_files': drafts,
			}
			if form.is_valid():
				submit_form = form.save(commit=False)
				submit_form.user_id = User.objects.get(pk=request.user.id)
				submit_form.process_id = Process.objects.get(pk=process_id)
				submit_form.save()
				response = HttpResponseRedirect(reverse('stepwise_detail', args=[process_id]))
			else:
				response = render(request, 'stepwise/stepwise_project_detail.html', context)		
	return response

def stepwise_comment_admin(request, process_id):
	redir = "/stepwise/stepwise_portal_admin/stepwise_project_detail_admin/"+str(process_id)+"/"
	response = stepwise_auth_user_in_group(request, "stepwise_manager", redir)
	if response == True:
		project = Process.objects.all().filter(pk=process_id)[0]
		if request.method == "POST":
			project = Process.objects.all().filter(pk=process_id)[0]
			documents = Prospectus.objects.all().filter(pk=project.prospectus_id.id)
			comments = Comment.objects.all().filter(process_id=process_id).order_by('date_created')
			drafts = Draft.objects.all().filter(process_id=process_id)
			form = stepwise_comment_form(request.POST or None, request.FILES or None)
			context = {
				'project': project,
				'documents': documents,
				'comment_form': form,
				'comments': comments,
				'draft_files': drafts,
			}
			if form.is_valid():
				submit_form = form.save(commit=False)
				submit_form.user_id = User.objects.get(pk=request.user.id)
				submit_form.process_id = Process.objects.get(pk=process_id)
				submit_form.save()
				response = HttpResponseRedirect(reverse('stepwise_project_detail_admin', args=[process_id]))
			else:
				response = render(request, 'stepwise/stepwise_portal_admin/stepwise_project_detail_admin/', context)
	return response

def stepwise_upload_draft(request, process_id):
	response = HttpResponseRedirect(reverse('stepwise_detail', args=[process_id]))
	if request.user.is_authenticated():
		project = Process.objects.all().filter(pk=process_id)[0]
		if request.user.id == project.user_id.id:
			form = upload_draft_form()
			context = {
				'project': project,
				'form': form,
			}
			if request.method == "POST":
				form = upload_draft_form(request.POST or None, request.FILES or None)
				context['form'] = form
				if form.is_valid():
					form = form.save(commit=False)
					form.draft_title = request.FILES['draft_file'].name
					form.process_id = Process.objects.get(pk=process_id)
					form.save()

					PFModel = Process.objects.get(pk=process_id)
					PFModel.percent_done = 42
					PFModel.current_step = 4
					PFModel.save()
					response = HttpResponseRedirect(reverse('stepwise_detail', args=[process_id]))
				else:
					response = render(request, 'stepwise/stepwise_upload_draft.html', context)
			else:
				response = render(request, 'stepwise/stepwise_upload_draft.html', context)
		else:
			err = "You do not have the proper credentials to view the requested page, please login to an account with the proper permissions and try again."
			redirect = '/stepwise/stepwise_detail/'+str(process_id)+'/'
			response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)			
	else:
		err = "You must be logged in to access stepwise, if you don't have a login, you can register by clicking the 'Register' button below."
		redirect = '/stepwise/stepwise_detail/'+str(process_id)+'/'
		response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	return response

def stepwise_upload_final(request, process_id):
	owner_id = Process.objects.filter(pk=process_id)[0].user_id.id
	print(owner_id)
	response = stepwise_auth_user_ownership(request, owner_id, '/stepwise/stepwise_detail/'+str(process_id)+'/')
	print(response)
	if response == True:
		project = Process.objects.filter(pk=process_id)[0]
		form = upload_final_form()
		context = {
			'project':project,
			'form':form,
		}
		if request.method == "POST":
			form = upload_final_form(request.POST or None, request.FILES or None)
			context['form'] = form
			if form.is_valid():
				form = form.save(commit=False)
				form.file_title = request.FILES['proposal_file'].name
				form.save()

				PFModel = Process.objects.get(pk=process_id)
				PFModel.percent_done = 71
				PFModel.current_step = 6
				PFModel.proposal_id = Proposal.objects.get(pk=form.id)
				PFModel.save()
				response = HttpResponseRedirect(reverse('stepwise_detail', args=[process_id]))
			else:
				response = render(request, 'stepwise/stepwise_upload_final_draft.html', context)
		else:
			response = render(request, 'stepwise/stepwise_upload_final_draft.html', context)
	return response

def stepwise_portal_admin(request):
	response = HttpResponseRedirect(reverse('stepwise_portal_admin'))
	if request.user.is_authenticated():
		#make sure user is a part of manager group
		group = Group.objects.get(name="stepwise_manager")
		if group in request.user.groups.all():
			projects = Process.objects.all().order_by('-date_created')
			context = {
				'projects': projects,
			}
			response = render(request, 'stepwise/stepwise_portal_admin.html', context)
		else:
			err = "You do not have the proper credentials to view the requested page, please login to an account with the proper permissions and try again."
			redirect = '/stepwise/stepwise_portal_admin/'
			response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	else:
		err = "You must be logged in to access stepwise, if you don't have a login, you can register by clicking the 'Register' button below."
		redirect = '/stepwise/stepwise_portal_admin/'
		response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	return response

def stepwise_project_delete(request, process_id):
	response = HttpResponseRedirect(reverse('stepwise_portal_admin'))
	if request.user.is_authenticated():
		#make sure user is a part of manager group
		group = Group.objects.get(name="stepwise_manager")
		if group in request.user.groups.all():
			projects = Process.objects.all().order_by('-date_created')
			context = {
				'projects': projects,
			}

			process = Process.objects.filter(pk=process_id)[0]
			if process.proposal_id != None and process.proposal_id != '':
				process.proposal_id.delete()
			if process.prospectus_id.file != None and process.prospectus_id.file != '':
				process.prospectus_id.file.delete()
			if process.prospectus_id != None and process.prospectus_id != '':
				process.prospectus_id.delete()

			process.delete()

			response = HttpResponseRedirect(reverse('stepwise_portal_admin'))
		else:
			err = "You do not have the proper credentials to perform that action, please login to an account with the proper permissions and try again."
			redirect = '/stepwise/stepwise_portal_admin/'
			response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	else:
		err = "You must be logged in to access stepwise, if you don't have a login, you can register by clicking the 'Register' button below."
		redirect = '/stepwise/stepwise_portal_admin/'
		response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	return response

def stepwise_project_detail_admin(request, process_id):
	response = stepwise_auth_user_in_group(request, "stepwise_manager", "/stepwise/stepwise_portal_admin/")
	if response == True:
		project = Process.objects.all().filter(pk=process_id)[0]
		prospectus = Prospectus.objects.all().filter(pk=project.prospectus_id.id)[0]
		if prospectus.file == '' or prospectus.file == None:
			prospectus = None
		comments = Comment.objects.all().filter(process_id=process_id).order_by('date_created')
		drafts = Draft.objects.all().filter(process_id=process_id)
		comment_form = stepwise_comment_form()
		context = {
			'project': project,
			'prospectus': prospectus,
			'comment_form': comment_form,
			'comments': comments,
			'draft_files': drafts,
		}
		response = render(request, 'stepwise/stepwise_project_detail_admin.html', context)
	return response

def review_prospectus_approve(request, process_id):
	response = stepwise_auth_user_in_group(request, "stepwise_manager", "/stepwise/stepwise_portal_admin/stepwise_project_detail_admin/"+str(process_id)+"/")
	if response == True:
		project = Process.objects.get(pk=process_id)
		project.percent_done = 28
		project.current_step = 3
		project.review_id = True
		project.save()
		#send the user an email
		response = HttpResponseRedirect(reverse('stepwise_project_detail_admin', args=[process_id]))
	return response

def review_prospectus_deny(request, process_id):
	response = stepwise_auth_user_in_group(request, "stepwise_manager", "/stepwise/stepwise_portal_admin/stepwise_project_detail_admin/"+str(process_id)+"/")
	if response == True:
		project = Process.objects.get(pk=process_id)
		project.percent_done = 0
		project.current_step = 1
		project.save()
		#send the user an email
		response = HttpResponseRedirect(reverse('stepwise_project_detail_admin', args=[process_id]))
	return response

def oweb_app_submitted(request, process_id):
	response = stepwise_auth_user_in_group(request, "stepwise_manager", "/stepwise/stepwise_portal_admin/stepwise_project_detail_admin/"+str(process_id)+"/")
	if response == True:
		project = Process.objects.get(pk=process_id)
		project.percent_done = 42
		project.current_step = 4
		project.save()
		#send the user an email
		response = HttpResponseRedirect(reverse('stepwise_project_detail_admin', args=[process_id]))
	return response

def evaluate_draft_approve(request, process_id):
	response = stepwise_auth_user_in_group(request, "stepwise_manager", "/stepwise/stepwise_portal_admin/stepwise_project_detail_admin/"+str(process_id)+"/")
	if response == True:
		project = Process.objects.get(pk=process_id)
		project.percent_done = 57
		project.current_step = 5
		project.save()
		#send the user an email
		response = HttpResponseRedirect(reverse('stepwise_project_detail_admin', args=[process_id]))
	return response

def evaluate_draft_deny(request, process_id):
	response = stepwise_auth_user_in_group(request, "stepwise_manager", "/stepwise/stepwise_portal_admin/stepwise_project_detail_admin/"+str(process_id)+"/")
	if response == True:
		project = Process.objects.get(pk=process_id)
		project.percent_done = 28
		project.current_step = 3
		project.save()
		#send the user an email
		response = HttpResponseRedirect(reverse('stepwise_project_detail_admin', args=[process_id]))
	return response

def final_approval_approve(request, process_id):
	response = stepwise_auth_user_in_group(request, "stepwise_manager", "/stepwise/stepwise_portal_admin/stepwise_project_detail_admin/"+str(process_id)+"/")
	if response == True:
		project = Process.objects.get(pk=process_id)
		project.percent_done = 100
		project.current_step = 7
		project.final_approval = True
		project.overall_status_id = Overall_status.objects.get(pk=3)
		project.save()
		#send the user an email
		response = HttpResponseRedirect(reverse('stepwise_project_detail_admin', args=[process_id]))
	return response
def final_approval_deny(request, process_id):
	response = stepwise_auth_user_in_group(request, "stepwise_manager", "/stepwise/stepwise_portal_admin/stepwise_project_detail_admin/"+str(process_id)+"/")
	if response == True:
		project = Process.objects.get(pk=process_id)
		project.percent_done = 100
		project.current_step = 7
		project.final_approval = False
		project.overall_status_id = Overall_status.objects.get(pk=4)
		project.save()
		#send the user an email
		response = HttpResponseRedirect(reverse('stepwise_project_detail_admin', args=[process_id]))
	return response



# The following three functions work together to determine the login status of a user. 
# They can be called separately, but the first two functions depend on the third to determine
# if a user is logged in at all. That being said, when a user is 'authenticated', the first
# check is to determine if a user is logged in. If the user is logged in, stepwise_auth_user_loggedin
# will return true and any subsequest checks will be made. If the user is logged in but the owner_id
# does not match the user's id or the user is not a member of the given group then instead an 
# httpresponseredirect will be returned. It is only in the event that True is returned that the user will
# have been thoroughly authenticated.
	# Returns:
	# 	False - User is not logged in and somehow managed to not fall into the if/else case in stepwise_auth_user_loggedin
	# 	HttpResponseRedirect - User is either not logged in, or has the wrong credentials. 
	# 	True - User is logged in and either is a member of the provided group or is the owner of the provided id
def stepwise_auth_user_in_group(request, grp, redir):
	response = stepwise_auth_user_loggedin(request, redir)
	if response == True:
		#make sure user is a part of manager group
		group = Group.objects.get(name=grp)
		if group in request.user.groups.all():
			response = True
		else:
			err = "You do not have the proper credentials, please login to an account with the proper permissions and try again."
			redirect = redir
			response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	return response
def stepwise_auth_user_ownership(request, owner_id, redir):
	response = stepwise_auth_user_loggedin(request, redir)
	if response == True:
		#make sure user id matches the owner id
		if request.user.id == owner_id:
			response = True
		else:
			err = "You do not have the proper credentials, please login to an account with the proper permissions and try again."
			redirect = redir
			response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	return response
def stepwise_auth_user_loggedin(request, redir):
	response = False
	if request.user.is_authenticated():
		response = True
	else:
		err = "You must be logged in to access stepwise, if you don't have a login, you can register by clicking the 'Register' button below."
		redirect = redir
		response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	return response

def generate_approval_letter(request):
	context = {
		'user_name': 'Joe Schmoe',
		'user_street_address': '111 Infiniti Ln.',
		'user_city_state_zip': 'Nowhere, NB, 88888',
		'project_name': "Jesse Steele's Mid-Summer Pool Project",
		'letter_content': 'At a regularly scheduled meeting of the Grande Ronde Model Watershed Board of Directors on May 9, 2017, your project UGR Bird Track Springs Fish Habitat Restoration was recommended for funding. The recommendation included allocations as follows: <br><br>OWEB FIP             $507,016<br>	BPA FY 2017    $1,503,539<br>		BPA FY 2018         $507,752<br><br>Please work with Tracy Hauser at BPA to confirm funding and input information in Pisces. An OWEB grant agreement will be made available for signatures shortly after the OWEB Board meeting in late July, barring unforeseen circumstances.<br><br>Congratulations and good luck.',
		'signer': 'Jeff Oveson',
		'cc_list': {'Jesse Steele, GRMW jesse@grmw.org', 'Tracy Hauser, BPA tlhauser@bpa.gov', 'Andrew Dutterer, OWEB andrew.dutterer@state.or.us'}
	}
	response = render(request, 'stepwise/approval_letter_template.html', context)
	return response

def stepwise_approval_letter(request, process_id):
	response = stepwise_auth_user_in_group(request, "stepwise_manager", "/stepwise/stepwise_portal_admin/stepwise_project_detail_admin/"+str(process_id)+"/")
	if response == True:
		project = Process.objects.get(pk=process_id)
		form = approval_letter_form(request.POST or None)
		context = {
			'project': project,
			'approval_letter_form': form,
		}
		response = render(request, 'stepwise/approval_letter_form.html', context)
	return response
