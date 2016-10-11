from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from home.models import *


def index(request):
	project_list = ProjectdbProject.objects.filter(publish=True).filter(Q(status_id=1) | Q(status_id=2)).order_by("-fiscalyear")[:10]
	year_list = PublicationsRipples.objects.all().distinct('year').order_by('-year')
	return render(request, 'home/index.html', {'projects': project_list, 'years': year_list})