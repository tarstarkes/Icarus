from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from django.http import HttpResponse
from django.db.models import Q
from html.parser import HTMLParser
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse

import os

def index(request):
	#get the username, password, redirect params
	user = request.GET.get("user")
	pwd = request.GET.get("pass")
	redirect = request.GET.get("redirect")
	err = request.GET.get("error")

	#go to the login page if there is nothing to authenticate
	if (err != None and err != ""):
		returnHtml = render(request, "user_login/login.html", {'error': err})
	else:
		returnHtml = render(request, "user_login/login.html")

	#user and pwd were not entered
	if(user != None and pwd != None):
		parser = HTMLParser()
		pwd = parser.unescape(pwd)
		user = parser.unescape(user)
		user=authenticate(username=user, password=pwd) #authenticate the username and password
		if user is not None:
			login(request, user) #log the user in
			returnHtml = HttpResponseRedirect("/")
			if(redirect != None and redirect != ""):
				#there is a redirect link
				redirect = parser.unescape(redirect)
				returnHtml = HttpResponseRedirect(redirect) #redirect the user to the requested page
		else:
			#user failed to authenticate
			print("going back to login")
			err="Sorry, but that username and password combination is invalid. Please check your credentials and try again or contact the server admin at infotech@gmail.com."
			returnHtml = render(request, "user_login/login.html", { 'error': err } )

	return returnHtml

def register(request):
	return render(request, "user_login/register.html")

def logout(request):

	return render(request, "")