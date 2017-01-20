from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render


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
		renderedTemplate = render(request, 'stepwise/stepwise_portal.html')
	else:
		renderedTemplate = render(request, 'user_login/stepwise_portal_login.html')
	return renderedTemplate
