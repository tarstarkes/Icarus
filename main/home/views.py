from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from home.models import *
from django.db.models import F


def index(request):
	project_list = ProjectdbProject.objects.filter(publish=True).filter(Q(status_id=1) | Q(status_id=2)).order_by("-fiscalyear")[:10]
	year_list = Ripples.objects.all().distinct('year').order_by('-year').values('year')
	ripple_list = serializers.serialize('json', Ripples.objects.all().order_by('-year'))
	ripple_article = serializers.serialize('json', Ripplesarticle.objects.all())
	return render(request, 'home/index.html', {'projects': project_list, 'years': year_list, 'ripples': ripple_list, 'articles': ripple_article})