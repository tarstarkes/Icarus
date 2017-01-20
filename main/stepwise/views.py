from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.urlresolvers import reverse
import user_login


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
		print("authenticated")
		response = render(request, 'stepwise/stepwise_portal.html')
	else:
		print("not authenticated")
		err = "You must be logged in to use stepwise, if you don't have a login, you can register by clicking the 'Register' button below"
		redirect = '/stepwise/stepwise_portal/'
		response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
		#response = render(request, 'user_login/login.html', {'error': err, 'redirect': redirect})
	return response
