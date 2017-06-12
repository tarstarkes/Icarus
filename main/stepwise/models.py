from django.db import models
from django.contrib.gis.db import models as gisModels
from django import forms
import datetime
import os
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Overall_status(models.Model):
	status = models.CharField(max_length=200)
	def __str__(self):
		return (self.status)

	class Meta:
		managed = True
		db_table = 'stepwise_overall_status'

def get_proposal_path(instance, filename):
	upload_dir = os.path.join( "static", "documents",  "stepwise", "proposals")
	if not os.path.exists(upload_dir):
		os.makedirs(upload_dir)
	return os.path.join(upload_dir, filename)

class Proposal(models.Model):
	file_title = models.CharField(max_length=100)
	proposal_file = models.FileField(upload_to=get_proposal_path)
	date_uploaded = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return (self.file_title)

	class Meta:
		managed = True
		db_table = 'stepwise_proposal_file'

def get_site_visit_path(instance, filename):
	upload_dir = os.path.join( "documents", "stepwise", "site_visits", str(User.id))
	if not os.path.exists(upload_dir):
		os.makedirs(upload_dir)
	return os.path.join(upload_dir, filename)

class Site_visit(models.Model):
	location = models.CharField(max_length=100)
	document = models.FileField(upload_to=get_site_visit_path)
	notes = models.TextField(blank=True, null=True)
	date = models.DateField()

	def __str__(self):
		return (self.location)

	class Meta:
		managed = True
		db_table = 'stepwise_site_visit'

class WorkSpecialties(models.Model):
	work_specialty = models.CharField(max_length=200)

	def __str__(self):
		return (self.work_specialty)

	class Meta:
		managed = True
		db_table = 'stepwise_work_specialty'

class WorkType(models.Model):
	work_type_desc = models.CharField(max_length=200)

	def __str__(self):
		return (self.work_type_desc)

	class Meta:
		managed = True
		db_table = 'stepwise_work_type'

class Permits_consults(models.Model):
	permit_consult_name = models.CharField(max_length=50)

	def __str__(self):
		return (self.permit_consult_name)

	class Meta:
		managed = True
		db_table = 'stepwise_permit_consult'

class Activities(models.Model):
	activity_number = models.IntegerField()
	activity_name = models.CharField(max_length=100)

	def __str__(self):
		return (str(self.activity_number)+". "+self.activity_name)

	class Meta:
		managed = True
		db_table = 'stepwise_restoration_activities'

class bsr(models.Model):
	bsr = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return (self.bsr)

	class Meta:
		managed = True
		db_table = 'stepwise_bsr'

class bsr_tier(models.Model):
	bsr_tier = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return (self.bsr_tier)

	class Meta:
		managed = True
		db_table = 'stepwise_bsr_tier'

def get_prospectus_upload_path(instance, filename):
	upload_dir = os.path.join( "static", "documents",  "stepwise", "prospectus")
	if not os.path.exists(upload_dir):
		os.makedirs(upload_dir)
	return os.path.join(upload_dir, filename)

class Prospectus(models.Model):
	title = models.CharField(max_length=200)
	tech_contact_name = models.CharField(max_length=50, blank=True, null=True)
	tech_contact_org = models.CharField(max_length=50, blank=True, null=True)
	phone_regex = RegexValidator(regex=r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$', message="Phone number must be entered in the form 'XXX-XXX-XXXX'. Area code is required.")
	tech_contact_ph = models.CharField(validators=[phone_regex], max_length=15, blank=True)
	tech_contact_email = models.EmailField(max_length=50, blank=True)
	opp_lead_name = models.CharField(max_length=50, null=True)
	opp_lead_org = models.CharField(max_length=50, blank=True, null=True)
	opp_lead_ph = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)
	opp_lead_email = models.EmailField(max_length=50, blank=True, null=True)
	landowners_contacted = models.NullBooleanField(blank=True)
	landowners_supportive = models.TextField(blank=True, null=True)
	landowners_contribution = models.TextField(blank=True, null=True)
	river_stream_name = models.CharField(max_length=100, blank=True, null=True)
	river_miles = models.CharField(max_length=20, blank=True, null=True)
	tributary_to = models.CharField(max_length=100, blank=True, null=True)
	bsr = models.ForeignKey(bsr, blank=True, null=True)
	bsr_tier = models.ForeignKey(bsr_tier, blank=True, null=True)
	original_atlas_opp_score = models.CharField(max_length=20, blank=True, null=True)
	original_atlas_opp_score_notes = models.TextField(blank=True, null=True)
	proposed_atlas_opp_score = models.CharField(max_length=20, blank=True, null=True)
	proposed_atlas_opp_score_notes = models.TextField(blank=True, null=True)
	restoration_activities = models.ManyToManyField(Activities, blank=True, related_name='activities')
	focal_species = models.TextField(blank=True, null=True)
	other_species = models.TextField(blank=True, null=True)
	project_description = models.TextField(blank=True, null=True)
	project_objectives = models.TextField(blank=True, null=True)
	major_risks = models.TextField(blank=True, null=True)
	permits_consultations = models.ManyToManyField(Permits_consults, blank=True)
	aniticipated_year_regex = RegexValidator(regex=r'^[0-9]{4}$', message='Anticipated Implementation Year must be numerical in the format XXXX, example: 2016.')
	anticipated_year = models.CharField(validators=[aniticipated_year_regex], max_length=4, blank=True, null=True)
	monitoring = models.TextField(blank=True, null=True)
	multi_phase = models.NullBooleanField(blank=True)
	multi_phase_desc = models.TextField(blank=True, null=True)
	ph1_standalone = models.NullBooleanField(blank=True)
	phase_approach_value_loss = models.TextField(blank=True, null=True)
	project_cost = models.CharField(max_length=20, blank=True, null=True)
	bpa_funding = models.CharField(max_length=20, blank=True, null=True)
	fip_funding = models.CharField(max_length=20, blank=True, null=True)
	CHOICES = ((True, 'Yes'), (False, 'No'))
	grmw_design_funds = models.NullBooleanField(choices=CHOICES, null=True, default=None)
	funds_options = (('Option 1', 'Option 1'), ('Option 2', 'Option 2'))
	funds_request_option = models.CharField(choices=funds_options, max_length=50, blank=True, null=True)
	work_type = models.ManyToManyField(WorkType, blank=True)
	work_specialties = models.ManyToManyField(WorkSpecialties, blank=True)
	current_step = models.IntegerField(blank=True, null=True)
	complete = models.BooleanField(default=False)
	file = models.FileField(upload_to=get_prospectus_upload_path, blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return (self.title)

	class Meta:
		managed = True
		db_table = 'stepwise_prospectus'

class Landowner(models.Model):
	prospectus_id = models.ForeignKey(Prospectus, null=True)
	user_id = models.ForeignKey(User, null=True)
	landowner_name = models.CharField(max_length=100)
	landowner_address = models.CharField(max_length=200, blank=True, null=True)
	phone_regex = RegexValidator(regex=r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$', message="Phone number must be entered in the form 'XXX-XXX-XXXX'. Area code is required.")
	landowner_phone = models.CharField(validators=[phone_regex],max_length=15, blank=True, null=True)
	landowner_email = models.EmailField(max_length=50, blank=True, null=True)

	def __str__(self):
		return (self.landowner_name)

	class Meta:
		managed = True
		db_table = 'stepwise_landowner'


def process_title(self):
	rtn = ''
	if self.prospectus_id:
		rtn = self.prospectus_id.title
	else:
		rtn = str(self.landowner_name)+" - "+str(self.date_created)
	return rtn

class Process(models.Model):
	user_id = models.ForeignKey(User)
	prospectus_id = models.ForeignKey(Prospectus, blank=True, null=True, on_delete=models.CASCADE)
	review = models.NullBooleanField(blank=True, default=False)
	evaluation = models.NullBooleanField(blank=True, default=False)
	site_visit_id = models.ForeignKey(Site_visit, blank=True, null=True)
	proposal_id = models.ForeignKey(Proposal, blank=True, null=True, on_delete=models.CASCADE)
	final_approval = models.NullBooleanField(blank=True, default=False)
	overall_status_id = models.ForeignKey(Overall_status)
	percent_done = models.IntegerField()
	date_created = models.DateTimeField(auto_now_add=True)
	current_step = models.IntegerField(blank=True, default=1)

	def __str__(self):
		return (process_title(self))

	class Meta:
		managed = True
		ordering = ['-date_created']
		db_table = 'stepwise_process'

def get_draft_path(instance, filename):
	upload_dir = os.path.join( "static", "documents", "stepwise", "draft_proposals", str(instance.process_id.id))
	if not os.path.exists(upload_dir):
		os.makedirs(upload_dir)
	return os.path.join(upload_dir, filename)

class Draft(models.Model):
	draft_title = models.CharField(max_length=200, blank=True)
	process_id = models.ForeignKey(Process, null=True)
	draft_file = models.FileField(upload_to=get_draft_path)
	date_uploaded = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return (self.draft_title)

	class Meta:
		managed = True
		db_table = 'stepwise_draft_file'

def get_doc_path(instance, filename):
	upload_dir = os.path.join( "static", "documents", "stepwise", "comments", str(instance.user_id.id))
	if not os.path.exists(upload_dir):
		os.makedirs(upload_dir)
	return os.path.join(upload_dir, filename)

class Comment(models.Model):
	subject = models.CharField(max_length=200) 
	content = models.TextField(blank=True, null=True)
	user_id = models.ForeignKey(User, blank=True)
	attachment = models.FileField(blank=True, upload_to=get_doc_path, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	process_id = models.ForeignKey(Process)

	def __str__(self):
		return (str(self.user_id.username)+" - "+str(self.date_created))

	class Meta:
		managed = True
		ordering = ['-date_created']
		db_table = 'stepwise_comment'

