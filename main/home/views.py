from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from home.models import *
from django.db.models import F


def index(request):
	project_list = ProjectdbProject.objects.filter(publish=True).filter(Q(status_id=1) | Q(status_id=2)).order_by("-fiscalyear")[:10]
	year_list = Ripples.objects.all().distinct('year').order_by('-year').values('year')
	ripple_list = Ripples.objects.all()
	ripple_query = Ripplesarticle.objects.filter(ripples_id=F('ripples_id_id'))
	ripples = serializers.serialize('json', ripple_query)
	return render(request, 'home/index.html', {'projects': project_list, 'years': year_list, 'ripples': ripples})