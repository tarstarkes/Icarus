from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.urlresolvers import reverse
import user_login
from atlas.models import *
from atlas.forms import *
from random import randint
from weasyprint import HTML, CSS
from django.template.loader import get_template
from django.template import RequestContext
from django.conf import settings
from django.core.files import File
from django.contrib.auth.models import Group
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.mail import send_mail
import os
from django.conf import settings
import datetime
from django.forms import modelformset_factory

# Create your views here.
def change_log(request, atlas_id, msg):
	log = atlas_change_log.objects.filter(atlas_id=atlas_id)[0]
	fileURL = os.path.join(str(settings.BASE_DIR), str(log.change_log_file))
	file = open(fileURL, 'a')
	file.write(msg+' -- [ '+str(datetime.datetime.now().time())+" ]\n")
	file.close()

def get_assoc_group(atlas_id):
	rtn = "Atlas_Admin"
	if atlas_id == 2:
		rtn = "Atlas_UGR_Manage"
	elif atlas_id == 3:
		rtn = "Atlas_Wallowa_Manage"
	elif atlas_id == 4:
		rtn = "Atlas_CC_Manage"
	return rtn

def index(request):
	response = atlas_auth_user_loggedin(request, '/atlas/')
	if response == True:
		#only return the atlases that the user is supposed to have access to
		wallowa_manage = atlas_auth_user_in_group(request, "Atlas_Wallowa_Manage", '/atlas/')
		wallowa_view = atlas_auth_user_in_group(request, "Atlas_Wallowa_View", '/atlas/')
		ugr_manage = atlas_auth_user_in_group(request, "Atlas_UGR_View", '/atlas/')
		ugr_view = atlas_auth_user_in_group(request, "Atlas_UGR_View", '/atlas/')
		cc_manage = atlas_auth_user_in_group(request, "Atlas_CC_View", '/atlas/')
		cc_view = atlas_auth_user_in_group(request, "Atlas_CC_View", '/atlas/')
		admin = atlas_auth_user_in_group(request, "Atlas_Admin", '/atlas/')
		query_set = atlas.objects.none()
		if(wallowa_manage == True or wallowa_view == True or admin == True):
			query_set = query_set | atlas.objects.filter(pk=3)
		if(ugr_manage == True or ugr_view == True or admin == True):
			query_set = query_set | atlas.objects.filter(pk=2)
		if(cc_manage == True or cc_view == True or admin == True):
			query_set = query_set | atlas.objects.filter(pk=4)

		context = {
			'atlases': query_set
		}
		response = render(request, 'atlas/index.html', context)
	return response

def atlas_auth_user_in_group(request, grp, redir):
	response = atlas_auth_user_loggedin(request, redir)
	if response == True:
		#make sure user is a part of manager group
		group = Group.objects.get(name=grp)
		if group in request.user.groups.all():
			response = True
		else:
			err = "You do not have the proper credentials, please using an account with the proper permissions and try again."
			redirect = redir
			response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	return response

def atlas_auth_user_ownership(request, owner_id, redir):
	response = atlas_auth_user_loggedin(request, redir)
	if response == True:
		#make sure user id matches the owner id
		if request.user.id == owner_id:
			response = True
		else:
			err = "You do not have the proper credentials, please login using an account with the proper permissions and try again."
			redirect = redir
			response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	return response

def atlas_auth_user_loggedin(request, redir):
	response = False
	if request.user.is_authenticated():
		response = True
	else:
		err = "You must be logged in to access the Restoration Atlas, if you don't have a login, you can register by clicking the 'Register' button below."
		redirect = redir
		response = HttpResponseRedirect("/login/?error="+err+"&redirect="+redirect)
	return response
def atlas_auth_user_in_atlas(request, atlas_id):
	response = False
	atlas_id = int(atlas_id)
	if atlas_id == 2:
		UGR_view = atlas_auth_user_in_group(request, "Atlas_UGR_View", "/atlas/")
		UGR_manage = atlas_auth_user_in_group(request, "Atlas_UGR_Manage", "/atlas/")
		if UGR_view == True or UGR_manage == True:
			response = True
		else:
			response = atlas_auth_user_in_group(request, "Atlas_UGR_View", "/atlas/")
	elif atlas_id == 3:
		Wallowa_view = atlas_auth_user_in_group(request, "Atlas_Wallowa_View", "/atlas/")
		Wallowa_manage = atlas_auth_user_in_group(request, "Atlas_Wallowa_Manage", "/atlas/")
		if Wallowa_view == True or Wallowa_manage == True:
			response = True
		else:
			response = atlas_auth_user_in_group(request, "Atlas_Wallowa_View", "/atlas/")
	elif atlas_id == 4:
		CC_view = atlas_auth_user_in_group(request, "Atlas_CC_View", "/atlas/")
		CC_manage = atlas_auth_user_in_group(request, "Atlas_CC_Manage", "/atlas/")
		if CC_view == True or CC_manage == True:
			response = True
		else:
			response = atlas_auth_user_in_group(request, "Atlas_CC_View", "/atlas/")

	#is user an atlas administrator
	if atlas_auth_user_in_group(request, "Atlas_Admin", "/atlas/") == True or response == True:
		response = True
	else:
		response = atlas_auth_user_in_group(request, "Atlas_Admin", "/atlas/")

	return response

def atlas_auth_user_is_manager(request, bsr_id=False, atlas_id=False):
	response = False
	if bsr_id != False:
		bsr = atlas_bsr.objects.filter(pk=bsr_id)[0]
		atlas_id = bsr.atlas_id.id
		atlas_id = int(atlas_id)

	if atlas_auth_user_in_group(request, "Atlas_UGR_Manage", "/atlas/") == True and atlas_id == 2:
		response = True
	elif atlas_auth_user_in_group(request, "Atlas_CC_Manage", "/atlas/") == True and atlas_id == 4:
		response = True
	elif atlas_auth_user_in_group(request, "Atlas_Wallowa_Manage", "/atlas/") == True and atlas_id == 3:
		response = True

	if atlas_auth_user_in_group(request, "Atlas_Admin", "/atlas/") == True or response == True:
		response = True
	else:
		response = atlas_auth_user_in_group(request, "Atlas_Admin", "/atlas/")
	return response

def generate_ras(request, bsr_id):
	ras = restoration_actions.objects.all()
	for ra in ras:
		form = restoration_actions_score(None)
		form.restoration_action_id = restoration_actions.objects.get(pk=ra.id)
		form.bsr_id = atlas_bsr.objects.get(pk=bsr_id)
		form.save()
	return True


def BSR_view(request, atlas_id):
	response = atlas_auth_user_loggedin(request, '/atlas/')
	if response == True:
		response = atlas_auth_user_in_atlas(request, atlas_id)
		if response == True:
			atlas_set = atlas.objects.filter(pk=atlas_id)[0]
			all_bsr = atlas_bsr.objects.filter(atlas_id=atlas_id).order_by("tier_id__tier")
			all_opps = bsr_opportunity.objects.filter(bsr_id__atlas_id__pk=atlas_id).order_by("bsr_id")
			perm = get_assoc_group(atlas_id)
			bsr_form = atlas_bsr_form(None)
			lethok = (("Lethal", "Lethal"), ("Ok", "Ok"))
			norm = (("Poor", "Poor"), ("Fair", "Fair"), ("Good", "Good"), ("Excellent", "Excellent"), ("TBD", "TBD"))
			if atlas_id == "4":
				bsr_form.fields['current_temp'].choices = lethok
			else: 
				bsr_form.fields['current_temp'].choices = norm

			context = {
				'bsr_form': bsr_form,
				'perm': perm,
				'atlas': atlas_set,
				'all_bsr': all_bsr,
				'opportunities': all_opps,
			}
			response = render(request, 'atlas/bsr_view.html', context)
	return response

def add_new_bsr(request, atlas_id):
	response = atlas_auth_user_is_manager(request, False, atlas_id)
	if response == True:
		if request.method == "POST":
			bsr_form = atlas_bsr_form(request.POST or None)
			if bsr_form.is_valid():
				form = bsr_form.save(commit=False)
				form.atlas_id = atlas.objects.get(pk=atlas_id)
				form.save()
				generate_ras(request, form.id)
			else:
				print(bsr_form.errors)
		response = HttpResponseRedirect("/atlas/go_to_atlas/"+str(atlas_id))
	return response

def get_access(request, atlas):
	response = atlas_auth_user_loggedin(request, '/atlas/')
	if response == True:
		#send email to infotech@grmw.org with user info
		sent = send_mail(
			'Request for Access',
			request.user.first_name+" "+request.user.last_name+" has requested access to the "+atlas+" Restoration Atlas."+" Username: "+request.user.username+".",
			request.user.email,
			['infotech@grmw.org'],
			fail_silently=False,
		)
		if sent == 1:
			response = render(request, 'atlas/request_access_success.html')
		else:
			response = render(request, 'atlas/request_access_failure.html')
	return response

def detailed_bsr_context(request, bsr_id):
	utils_query = utilization_score.objects.filter(utilization_id__bsr_id=bsr_id)
	utilizations = utils_query.order_by("utilization_id__utilization_name").distinct('utilization_id__utilization_name')
	utils = utils_query.order_by("species", "utilization_id__utilization_name").distinct('species')
	u_ratings = utils_query.order_by("utilization_id__utilization_name", "species")
	bsr = atlas_bsr.objects.filter(pk=bsr_id)
	life_stages= life_stage.objects.filter(bsr_id=bsr_id).order_by("species", "life_stage_name")
	lf_query = limiting_factor_score.objects.filter(limiting_factor_instance_id__bsr_id=bsr_id)
	lf_score = lf_query
	lfs = lf_query.distinct("limiting_factor_instance_id__limiting_factor_id")
	rest_action = restoration_actions_score.objects.filter(bsr_id=bsr_id).order_by("restoration_action_id__action_number")
	comments = bsr_comment.objects.filter(bsr_id=bsr_id).order_by("date_created")
	comment_form = bsr_comment_form(request.POST or None, request.FILES or None)
	opportunities = bsr_opportunity.objects.filter(bsr_id=bsr_id).order_by("opportunity_name")
	context = {
		'utilizations': utilizations,
		'utils': utils,
		'u_ratings': u_ratings, 
		'bsr': bsr,
		'life_stages': life_stages,
		'lf_score': lf_score,
		'lfs': lfs,
		'rest_action': rest_action,
		'comment_form': comment_form,
		'comments': comments,
		'opportunities': opportunities,
	}
	return context

def BSR_detail(request, bsr_id):
	bsr = atlas_bsr.objects.filter(pk=bsr_id)[0]
	response = atlas_auth_user_in_atlas(request, bsr.atlas_id.id)
	if response == True:
		context = detailed_bsr_context(request, bsr_id)
		context['perm'] = (get_assoc_group(bsr.atlas_id.id))
		response = render(request, 'atlas/bsr_detail.html', context)
	return response

def bsr_create_comment(request, bsr_id):
	bsr = atlas_bsr.objects.filter(pk=bsr_id)[0]
	response = atlas_auth_user_in_atlas(request, bsr.atlas_id.id)
	if response == True:
		if request.method == "POST":
			form = bsr_comment_form(request.POST or None, request.FILES or None)
			if form.is_valid():
				submit_form = form.save(commit=False)
				submit_form.user_id = User.objects.get(pk=request.user.id)
				submit_form.bsr_id = atlas_bsr.objects.get(pk=bsr_id)
				submit_form.save()
				response = HttpResponseRedirect("/atlas/go_to_bsr/"+str(bsr_id))
			else:
				response = BSR_detail(request, bsr_id)
	return response

def opportunity_detail(request, opp_id):
	opportunity = bsr_opportunity.objects.filter(pk=opp_id)[0]
	atlas_id = opportunity.bsr_id.atlas_id.id
	response = atlas_auth_user_in_atlas(request, atlas_id)
	if response == True:
		rest_actions = bsr_opportunity_action.objects.filter(opportunity_id=opp_id).order_by("action_id__restoration_action_id__action_number")
		context = {
			'opportunity': opportunity,
			'rest_actions': rest_actions,
			'perm': get_assoc_group(atlas_id),
		}
		response = render(request, 'atlas/opportunity_detail.html', context)
	return response

def edit_bsr(request, bsr_id):
	response = atlas_auth_user_is_manager(request, bsr_id)
	if response == True:
		context = detailed_bsr_context(request, bsr_id)

		p_forms = modelformset_factory(life_stage, fields='__all__', extra=0)
		p_formset = p_forms(queryset=life_stage.objects.filter(bsr_id=bsr_id))

		util_forms = modelformset_factory(utilization_score, fields='__all__', extra=0)
		util_formset = util_forms(queryset=utilization_score.objects.filter(utilization_id__bsr_id=bsr_id))

		lf_forms = modelformset_factory(limiting_factor_score, fields='__all__', extra=0)
		lf_formset = lf_forms(queryset=limiting_factor_score.objects.filter(limiting_factor_instance_id__bsr_id=bsr_id))

		ra_forms = modelformset_factory(restoration_actions_score, fields='__all__', extra=0)
		ra_formset = ra_forms(queryset=restoration_actions_score.objects.filter(bsr_id=bsr_id))

		p_addnew = periodicity_life_stage_form(request.POST or None)
		new_fish_util_form = utilization_form(request.POST or None)
		new_limiting_factor_form = limiting_factor_form(None)
		opp_add_new = new_opportunity_form(None)
		tier_form = bsr_tier_form(None)

		lf_instances = limiting_factor_instance.objects.filter(bsr_id=bsr_id)
		obj_id_list = []
		for instance in lf_instances:
			obj_id_list.append(instance.limiting_factor_id.id)
		new_limiting_factor_form.fields['limiting_factor_id'].queryset = limiting_factor.objects.exclude(pk__in=obj_id_list).order_by("sub_id")

		context['p_formset'] = p_formset
		context['util_formset'] = util_formset
		context['lf_formset'] = lf_formset
		context['ra_formset'] = ra_formset
		context['tier_form'] = tier_form
		context['new_fish_util_form'] = new_fish_util_form
		context['new_limiting_factor_form'] = new_limiting_factor_form
		context['p_addnew'] = p_addnew
		context['new_opp_form'] = opp_add_new
		response = render(request, 'atlas/edit_bsr_detail.html', context)

		if request.method=='POST':
			formset = p_forms(request.POST)
			if formset.is_valid():
				formset.save()
				response = HttpResponseRedirect("/atlas/edit_bsr/"+str(bsr_id))
				
	return response

def update_tier(request, bsr_id):
	response = atlas_auth_user_is_manager(request, bsr_id)
	bsr = atlas_bsr.objects.get(pk=bsr_id)
	if response == True:
		if request.method == 'POST':
			form = bsr_tier_form(instance=bsr, data=request.POST or None)
			if form.is_valid():
				form.save()
		response = HttpResponseRedirect("/atlas/edit_bsr/"+str(bsr_id))
	return response

def add_new_life_stage(request, bsr_id):
	response = atlas_auth_user_is_manager(request, bsr_id)
	if response == True:
		if request.method == 'POST':
			form = periodicity_life_stage_form(request.POST or None)
			if form.is_valid():
				form = form.save(commit=False)
				form.bsr_id = atlas_bsr.objects.get(pk=bsr_id)
				form.save()
				response = HttpResponseRedirect("/atlas/edit_bsr/"+str(bsr_id))
			else:
				response = edit_bsr(request, bsr_id)
		else:
			response = edit_bsr(request, bsr_id)
	return response

def delete_life_stage(request, life_stage_id):
	bsr_id = life_stage.objects.filter(pk=life_stage_id)[0].bsr_id.id
	response = atlas_auth_user_is_manager(request, bsr_id)
	if response == True:
		ls = life_stage.objects.get(pk=life_stage_id)
		ls.delete()
		response = HttpResponseRedirect("/atlas/edit_bsr/"+str(bsr_id))
	return response

def update_fish_use(request, bsr_id):
	response = atlas_auth_user_is_manager(request, bsr_id)
	if response == True:
		if request.method == 'POST':
			util_form = modelformset_factory(utilization_score, fields='__all__', extra=0)
			formset = util_form(request.POST or None)
			if formset.is_valid():
				formset.save()
				response = HttpResponseRedirect("/atlas/edit_bsr/"+str(bsr_id))
			else:
				response = edit_bsr(request, bsr_id)
		else:
			response = edit_bsr(request, bsr_id)
	return response

def add_new_fish_use(request, bsr_id):
	response = atlas_auth_user_is_manager(request, bsr_id)
	if response == True:
		if request.method == 'POST':
			form = utilization_form(request.POST or None)
			atlas_id = atlas_bsr.objects.get(pk=bsr_id).atlas_id.id
			if form.is_valid():
				form = form.save(commit=False)
				form.bsr_id = atlas_bsr.objects.get(pk=bsr_id)
				form.save()
				all_species = fish_use_scoring.objects.filter(atlas_id=atlas_id).distinct('species')
				##THIS IS AN ISSUE BECAUSE THE CATHERINE CREEK ATLAS IS NOT BY SPECIES, IT IS A SINGULAR SCORE
				for ls in all_species:
					u_form = utilization_score_form(None)
					u_form = u_form.save(commit=False)
					u_form.species = ls.species
					u_form.utilization_id = utilization.objects.get(pk=form.id)
					u_form.save()
				response = HttpResponseRedirect("/atlas/edit_bsr/"+str(bsr_id))
			else:
				response = edit_bsr(request, bsr_id)
		else:
			response = edit_bsr(request, bsr_id)
	return response

def delete_fish_use(request, util_id):
	util = utilization.objects.get(pk=util_id)
	bsr_id = util.bsr_id.id
	response = atlas_auth_user_is_manager(request, bsr_id)
	if response == True:
		util_scores = utilization_score.objects.filter(utilization_id=util)
		util_scores.delete()
		util.delete()
		response = HttpResponseRedirect('/atlas/edit_bsr/'+str(bsr_id))
	return response

def add_new_limiting_factor(request, bsr_id):
	response = atlas_auth_user_is_manager(request, bsr_id)
	if response == True:
		if request.method == 'POST':
			form = limiting_factor_form(request.POST or None)
			atlas_id = atlas_bsr.objects.get(pk=bsr_id).atlas_id.id
			if form.is_valid():
				form = form.save(commit=False)
				form.bsr_id = atlas_bsr.objects.get(pk=bsr_id)
				form.save()
				all_species = fish_use_scoring.objects.filter(atlas_id=atlas_id).distinct('species')
				##THIS IS AN ISSUE BECAUSE THE CATHERINE CREEK ATLAS IS NOT BY SPECIES, IT IS A SINGULAR SCORE
				for s in all_species:
					lf_form = limiting_factor_score_form(None)
					lf_form = lf_form.save(commit=False)
					lf_form.species = species.objects.get(pk=s.species.id)
					lf_form.limiting_factor_instance_id = limiting_factor_instance.objects.get(pk=form.id)
					lf_form.save()
					print("SAVED")
				response = HttpResponseRedirect("/atlas/edit_bsr/"+str(bsr_id))
			else:
				response = edit_bsr(request, bsr_id)
		else:
			response = edit_bsr(request, bsr_id)
	return response

def update_limiting_factors(request, bsr_id):
	response = atlas_auth_user_is_manager(request, bsr_id)
	if response == True:
		if request.method == 'POST':
			lf_form = modelformset_factory(limiting_factor_score, fields='__all__', extra=0)
			formset = lf_form(request.POST or None)
			if formset.is_valid():
				formset.save()
				response = HttpResponseRedirect("/atlas/edit_bsr/"+str(bsr_id))
			else:
				response = edit_bsr(request, bsr_id)
		else:
			response = edit_bsr(request, bsr_id)
	return response

def delete_limiting_factor(request, lf_id):
	lf = limiting_factor_instance.objects.get(pk=lf_id)
	bsr_id = lf.bsr_id.id
	response = atlas_auth_user_is_manager(request, bsr_id)
	if response == True:
		lf_scores = limiting_factor_score.objects.filter(limiting_factor_instance_id=lf)
		lf_scores.delete()
		lf.delete()
		response = HttpResponseRedirect('/atlas/edit_bsr/'+str(bsr_id))
	return response

def update_rest_actions(request, bsr_id):
	response = atlas_auth_user_is_manager(request, bsr_id)
	if response == True:
		if request.method == 'POST':
			rest_action_form = modelformset_factory(restoration_actions_score, fields='__all__', extra=0)
			formset = rest_action_form(request.POST or None)
			if formset.is_valid():
				formset.save()
				response = HttpResponseRedirect("/atlas/edit_bsr/"+str(bsr_id))
			else:
				print(formset.errors)
				response = edit_bsr(request, bsr_id)
		else:
			response = edit_bsr(request, bsr_id)
	return response

def add_new_opp(request, bsr_id):
	response = atlas_auth_user_is_manager(request, bsr_id)
	if response == True:
		if request.method == 'POST':
			form = new_opportunity_form(request.POST or None)
			if form.is_valid():
				form = form.save(commit=False)
				form.bsr_id = atlas_bsr.objects.get(pk=bsr_id)
				form.save()
				response = HttpResponseRedirect("/atlas/edit_bsr/"+str(bsr_id))
			else:
				response = edit_bsr(request, bsr_id)
		else:
			response = edit_bsr(request, bsr_id)
	return response

def edit_opp(request, opp_id):
	opportunity = bsr_opportunity.objects.get(pk=opp_id)
	response = atlas_auth_user_is_manager(request, opportunity.bsr_id.id)
	if response == True:
		opp_objs = bsr_opportunity_action.objects.filter(opportunity_id=opp_id)
		rest_actions = opp_objs.order_by("action_id__restoration_action_id__action_number")
		lf_form = opp_action_form(None)
		np_form = opp_np_form(None)
		water_form = opp_water_form(None)
		fc_form = opp_fc_form(None)
		comment_form = opp_comment_form(None)
		desc_form = opp_desc_form(None)
		ra_ids = []
		for ra in opp_objs:
			ra_ids.append(ra.action_id.id)
		lf_form.fields['action_id'].queryset = restoration_actions_score.objects.exclude(pk__in=ra_ids).filter(bsr_id=opportunity.bsr_id.id).order_by("restoration_action_id__action_number")
		opp_map_form = opp_map()
		context = {
			'fc_form': fc_form,
			'opp_comment_form': comment_form,
			'opp_desc_form': desc_form,
			'opp_water_form': water_form,
			'lf_form': lf_form,
			'np_form': np_form,
			'opportunity': opportunity,
			'rest_actions': rest_actions,
			'opp_map_form': opp_map,
		}
		response = render(request, "atlas/edit_opportunity.html", context)
	return response

def update_opp_map(request, opp_id):
	opportunity = bsr_opportunity.objects.get(pk=opp_id)
	response = atlas_auth_user_is_manager(request, opportunity.bsr_id.id)
	if response == True:
		if request.method == "POST":
			opp_map_form = opp_map(instance=opportunity, data=request.POST or None)
			if opp_map_form.is_valid():
				opp_map_form.save()
		response = HttpResponseRedirect("/atlas/edit_opp/"+str(opp_id))
	return response

def add_opp_limiting_factor(request, opp_id):
	opportunity = bsr_opportunity.objects.get(pk=opp_id)
	response = atlas_auth_user_is_manager(request, opportunity.bsr_id.id)
	if response == True:
		if request.method == "POST":
			lf_form = opp_action_form(request.POST or None)
			if lf_form.is_valid():
				form = lf_form.save(commit=False)
				form.opportunity_id = opportunity
				form.save()
		response = HttpResponseRedirect("/atlas/edit_opp/"+str(opp_id))
	return response

def update_opp_np(request, opp_id):
	opportunity = bsr_opportunity.objects.get(pk=opp_id)
	response = atlas_auth_user_is_manager(request, opportunity.bsr_id.id)
	if response == True:
		if request.method == "POST":
			np_form = opp_np_form(instance=opportunity, data=request.POST or None)
			if np_form.is_valid():
				np_form.save()
		response = HttpResponseRedirect("/atlas/edit_opp/"+str(opp_id))
	return response

def update_longitudinal_score(request, opp_id):
	opportunity = bsr_opportunity.objects.get(pk=opp_id)
	response = atlas_auth_user_is_manager(request, opportunity.bsr_id.id)
	if response == True:
		if request.method == "POST":
			water_form = opp_water_form(instance=opportunity, data=request.POST or None)
			if water_form.is_valid():
				water_form.save()
		response = HttpResponseRedirect("/atlas/edit_opp/"+str(opp_id))
	return response

def update_fc(request, opp_id):
	opportunity = bsr_opportunity.objects.get(pk=opp_id)
	response = atlas_auth_user_is_manager(request, opportunity.bsr_id.id)
	if response == True:
		if request.method == "POST":
			fc_form = opp_fc_form(instance=opportunity, data=request.POST or None)
			if fc_form.is_valid():
				fc_form.save()
		response = HttpResponseRedirect("/atlas/edit_opp/"+str(opp_id))
	return response

def update_opp_comment(request, opp_id):
	opportunity = bsr_opportunity.objects.get(pk=opp_id)
	response = atlas_auth_user_is_manager(request, opportunity.bsr_id.id)
	if response == True:
		if request.method == "POST":
			comment_form = opp_comment_form(instance=opportunity, data=request.POST or None)
			if comment_form.is_valid():
				comment_form.save()
		response = HttpResponseRedirect("/atlas/edit_opp/"+str(opp_id))
	return response

def update_opp_desc(request, opp_id):
	opportunity = bsr_opportunity.objects.get(pk=opp_id)
	response = atlas_auth_user_is_manager(request, opportunity.bsr_id.id)
	if response == True:
		if request.method == "POST":
			desc_form = opp_desc_form(instance=opportunity, data=request.POST or None)
			if desc_form.is_valid():
				desc_form.save()
		response = HttpResponseRedirect("/atlas/edit_opp/"+str(opp_id))
	return response

def delete_lf_score(request, lf_id):
	lf = bsr_opportunity_action.objects.get(pk=lf_id)
	bsr_id = lf.opportunity_id.bsr_id.id
	response = atlas_auth_user_is_manager(request, bsr_id)
	if response == True:
		lf.delete()
		response = HttpResponseRedirect('/atlas/edit_opp/'+str(lf.opportunity_id.id))
	return response

def atlas_opp_map(request, atlas_id):
	response = atlas_auth_user_in_atlas(request, atlas_id)
	if response == True:
		this_atlas = atlas.objects.get(pk=atlas_id)
		opps = bsr_opportunity.objects.filter(bsr_id__atlas_id__id=atlas_id)
		context = {
			'atlas': this_atlas,
			'opportunities': opps,
		}
		response = render(request, 'atlas/atlas_opportunity_map.html', context)
	return response