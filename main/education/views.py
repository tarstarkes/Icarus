from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from home.models import *
from data.models import *
from django.db.models import Q
from html.parser import HTMLParser
from django.contrib.gis.shortcuts import render_to_kml
from django.conf import settings

import simplekml
import mimetypes
import os

def index(request):
	return render(request, "education/index.html")