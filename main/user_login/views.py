from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from django.http import HttpResponse
from django.db.models import Q
from html.parser import HTMLParser
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.core.urlresolvers import reverse

import os

def index(request):
	#get the username, password, redirect params
	user = request.GET.get("user")
	pwd = request.GET.get("pass")
	redirect = request.GET.get("redirect")
	err = request.GET.get("error")
	variableList = {}

	#go to the login page if there is nothing to authenticate
	if (err != None and err != ""):
		variableList['error'] = err
	if (redirect != None and redirect != ""):
		variableList['redirect'] = redirect
	
	returnHtml = render(request, "user_login/login.html", variableList)

	#user and pwd were not entered
	if(user != None and pwd != None):
		parser = HTMLParser()
		pwd = parser.unescape(pwd)
		user = parser.unescape(user)
		user=authenticate(username=user, password=pwd) #authenticate the username and password
		print(redirect)
		#user authenticated successfully, there should be no errors beyond this point so we may use HttpResponseRedirect without fear of losing an error message
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
			variableList['error'] = "Sorry, but that username and password combination is invalid. Please check your credentials and try again or contact the server admin at infotech@gmail.com."
			returnHtml = render(request, "user_login/login.html", variableList)

	return returnHtml

def register(request):
	return render(request, "user_login/register.html")

def logout(request):
	django_logout(request)
	return HttpResponseRedirect("/login/")