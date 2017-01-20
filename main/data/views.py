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
	#database calls for general queries needed for database page
	project_list = Project.objects.all().select_related().filter(publish=True).order_by("-fiscalyear")
	year_list = Project.objects.all().filter(publish=True).distinct("fiscalyear").order_by("-fiscalyear")
	org_list = Organization.objects.all().select_related().filter(orgrole_id=1).distinct("orgtype_id_id__name").order_by("orgtype_id_id__name")
	all_orgs = Organization.objects.all().select_related().filter(orgrole_id=1).order_by("orgtype_id_id__name")

	#get any filter criteria for the queries
	search = request.GET.get("search")
	year = request.GET.get("yr")
	org = request.GET.get("org")

	#apply filters
	if(search != '' and search != None):
		parser = HTMLParser() #used to turn character references back into characters
		search = parser.unescape(search)#unescape any escaped character for the search
		project_list = project_list.filter(Q(name__icontains=search))
	if(year != None and year != '-- Fiscal Year --'):
		project_list = project_list.filter(Q(fiscalyear__icontains=year))
	if(org != None and org != '-- Sponsor --'):
		project_list = project_list.filter(Q(organization__orgtype_id__id=org), Q(organization__orgrole_id=1))

	#return the queried data along with the data the user used for the query
	return render(request, 'data/projectDatabase.html', {
		'projects': project_list, 
		'years': year_list,
		'orgs': org_list,
		'orgs_all': all_orgs,
		'chosen_year': year, 
		'chosen_search': search,
		'chosen_org': org,
		})

def project_detail(request, project_id):
	project = Project.objects.all().select_related().filter(id=project_id)
	contacts = Contact.objects.all().select_related().filter(project_id=project_id)
	orgs = Organization.objects.all().select_related().filter(project_id=project_id)
	documents = Document.objects.all().select_related().filter(project_id_id=project_id)
	contracts = Contract.objects.all().select_related().filter(project_id_id=project_id)
	project_points = Site.objects.all().select_related().filter(project_id=project_id)
	project_images = Image.objects.all().select_related().filter(project_id_id=project_id)
	project_videos = Video.objects.all().select_related().filter(project_id_id=project_id)
	project_ortho = Ortho.objects.all().select_related().filter(project_id_id=project_id).first()

	return render(request, 'data/projectDetail.html', {
		'project': project[0],
		'docs': documents,
		'contacts': contacts,
		'organizations': orgs,
		'contracts': contracts,
		'sites': project_points,
		'images': project_images,
		'videos': project_videos,
		'ortho': project_ortho
		})


def return_kml(request, project_id, site_id):
	project = Project.objects.get(pk=project_id)
	site = Site.objects.get(pk=site_id)

	kml = simplekml.Kml()
	kml.newpoint(name=project.name, coords = [(site.getLong(), site.getLat())])
	print(os.getcwd())
	kml.save(os.path.join('static/kml/'+project_id+site_id+'.kml'))

	mimetypes.init()
	
	fsock = open(os.path.join('static/kml/'+project_id+site_id+'.kml'), 'r')
	response = HttpResponse(fsock, content_type="application/vnd.google-earth.kml+xml")
	response['Content-Disposition'] = "attachment; filename="+project.name+".kml"
	return response

def assessments(request):
	return render(request, 'data/assessments.html')

def precipFlow(request):
	return render(request, 'data/precipFlow.html')