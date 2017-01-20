from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db.models import Q
from html.parser import HTMLParser
from django.conf import settings

import os

def index(request):
	return render(request, "user_login/login.html")

def register(request):
	return render(request, "user_login/register.html")