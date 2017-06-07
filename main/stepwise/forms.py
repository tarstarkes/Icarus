#forms.py
from django import forms
from stepwise.models import *
import re
from django.utils.safestring import mark_safe

class process_form(forms.ModelForm):
	class Meta:
		model = Process
		exclude = ['date_created',]
		
class prospectus_step_1(forms.ModelForm):
	class Meta:
		model = Prospectus
		fields = ['title', 'tech_contact_name', 'tech_contact_org', 'tech_contact_ph', 'tech_contact_email']
		labels = {
			"title": "3-8 words that describe the type of project and location, including stream name (i.e. Catherine Creek RM44 Restoration Project)",
			"tech_contact_name": "List a qualified person whom GRMW can contact with technical questions regarding this opportunity. This may or may not be the same person as the Opportunity Lead",
			"tech_contact_org": "What organization (if any) does the Technical Contact belong to?",
			"tech_contact_ph": "Technical Contact Phone Number",
			"tech_contact_email": "Technical Contact Email Address",
		}
		help_text = {
			"title": "The title of the prospectus will also become the title of the project in the 'My Projects' section of Stepwise."
		}
	def __init__(self, *args, **kwargs):
		super(prospectus_step_1, self).__init__(*args, **kwargs)
		self.fields['title'].widget = forms.TextInput(attrs={
			'placeholder': 'Project Title'
			})
		self.fields['tech_contact_name'].widget = forms.TextInput(attrs={
			'placeholder': 'Technical Contact Full Name'
			})
		self.fields['tech_contact_org'].widget = forms.TextInput(attrs={
			'placeholder': 'Technical Contact Organization'
			})
		self.fields['tech_contact_ph'].widget = forms.TextInput(attrs={
			'placeholder': 'Technical Contact Phone'
			})
		self.fields['tech_contact_email'].widget = forms.TextInput(attrs={
			'placeholder': 'Technical Contact Email'
			})


class prospectus_step_2(forms.ModelForm):
	class Meta:
		model = Prospectus
		fields = ['opp_lead_name', 'opp_lead_org', 'opp_lead_ph', 'opp_lead_email']
		labels = {
			"opp_lead_name": "List the project sponsor. This may or may not be the same person as the Technical Contact",
			"opp_lead_org": "What organization (if any) does the Opportunity Lead belong to?",
			"opp_lead_ph": "Opportunity Lead Phone Number",
			"opp_lead_email": "Opportunity Lead Email Address"
		}

	def __init__(self, *args, **kwargs):
		super(prospectus_step_2, self).__init__(*args, **kwargs)
		self.fields['opp_lead_name'].widget = forms.TextInput(attrs={
			'placeholder': 'Opportunity Lead Name'
			})
		self.fields['opp_lead_org'].widget = forms.TextInput(attrs={
			'placeholder': 'Opportunity Lead Organization'
			})
		self.fields['opp_lead_ph'].widget = forms.TextInput(attrs={
			'placeholder': 'Opportunity Lead Phone'
			})
		self.fields['opp_lead_email'].widget = forms.TextInput(attrs={
			'placeholder': 'Opportunity Lead Email'
			})

class prospectus_step_3(forms.ModelForm):
	class Meta:
		model = Prospectus
		fields = ['landowners_contacted', 'landowners_supportive', 'landowners_contribution']
		labels = {
			'landowners_contacted': 'Have all landowners been contacted?',
			'landowners_supportive': 'Are all landowners supportive?',
			'landowners_contribution': 'How will the landowner be contributing?'
		}

class prospectus_add_landowner(forms.ModelForm):
	class Meta:
		model = Landowner
		exclude = ['prospectus_id', 'user_id']
		labels = {
			'landowner_name': "Full name of the landowner involved",
			'landowner_address': "Full address of the landowner involved",
			'landowner_phone': "Landowner's Phone Number",
			'landowner_email': "Landowner's Email",
		}

	def __init__(self, *args, **kwargs):
		super(prospectus_add_landowner, self).__init__(*args, **kwargs)
		self.fields['landowner_name'].widget = forms.TextInput(attrs={
			'placeholder': "Landowner's Full Name"
			})
		self.fields['landowner_address'].widget = forms.TextInput(attrs={
			'placeholder': "Landowner's Full Address"
			})
		self.fields['landowner_phone'].widget = forms.TextInput(attrs={
			'placeholder': "Landowner's Phone Number"
			})
		self.fields['landowner_email'].widget = forms.TextInput(attrs={
			'placeholder': "Landowner's Email Address"
			})

class prospectus_step_4(forms.ModelForm):
	class Meta:
		model = Prospectus
		fields = ['river_stream_name', 'river_miles', 'tributary_to']
		labels = {
			'river_stream_name': "Name of River/Stream",
			'river_miles': "River Miles",
			'tributary_to': "This River/Stream is a tributary to which River?",
		}
	def __init__(self, *args, **kwargs):
		super(prospectus_step_4, self).__init__(*args, **kwargs)
		self.fields['river_stream_name'].widget = forms.TextInput(attrs={
			'placeholder': "River/Stream Name"
			})
		self.fields['river_miles'].widget = forms.TextInput(attrs={
			'placeholder': "Example: RM44 - RM65"
			})
		self.fields['tributary_to'].widget = forms.TextInput(attrs={
			'placeholder': "Tributary to"
			})

class prospectus_step_5(forms.ModelForm):
	class Meta:
		model = Prospectus
		fields = ['bsr','bsr_tier', 'original_atlas_opp_score', 'original_atlas_opp_score_notes', 'proposed_atlas_opp_score', 'proposed_atlas_opp_score_notes']
		labels = {
			'bsr': 'Biologically Significant Reach - If the project will take place in more than one BSR please select the one where the majority of the project will take place.',
			'bsr_tier': 'BSR Tier - What Tier is the BSR in which the majority of the project is being implemented?',
			'original_atlas_opp_score': 'Original Atlas Opportunity Score - What was the initial opportunity score in the scoring matrix?',
			'original_atlas_opp_score_notes': 'Original Atlas Opportunity Score Notes (if any)',
			'proposed_atlas_opp_score': 'Proposed Atlas Opportunity Score - After initial concepts have been discussed with the landower what is the score?',
			'proposed_atlas_opp_score_notes': 'Proposed Atlas Opportunity Score Notes (if any)',
		}

	def __init__(self, *args, **kwargs):
		super(prospectus_step_5, self).__init__(*args, **kwargs)
		self.fields['original_atlas_opp_score'].widget = forms.TextInput(attrs={
			'placeholder': "Original Score"
			})
		self.fields['proposed_atlas_opp_score'].widget = forms.TextInput(attrs={
			'placeholder': "Proposed Score"
			})

class prospectus_step_6(forms.ModelForm):
	class Meta:
		model = Prospectus
		fields = ['restoration_activities']
		labels = {
			'restoration_activities': 'Restoration Activities - Check all that apply'
		}
		widgets = {
			'restoration_activities': forms.CheckboxSelectMultiple()
		}

	def __init__ (self, *args, **kwargs):
		super(prospectus_step_6, self).__init__(*args, **kwargs)
		self.fields['restoration_activities'].empty_label = None

class prospectus_step_7(forms.ModelForm):
	class Meta:
		model = Prospectus
		fields = ['focal_species', 'other_species']
		labels = {
			'focal_species': 'Focal Species - Enter the focal species for this project, if there is more than one, please separate species with commas.',
			'other_species': 'Other Species - Enter any other species that will benefit from this project, if there is more than one, please separate with commas.',
		}
	def __init__(self, *args, **kwargs):
		super(prospectus_step_7, self).__init__(*args, **kwargs)
		self.fields['focal_species'].widget = forms.Textarea(attrs={
			'placeholder': "Snake River Spring Chinook Salmon, Snake River Summer Steelhead, Bull Trout, Lamprey, etc..."
			})
		self.fields['other_species'].widget = forms.Textarea(attrs={
			'placeholder': "Snake River Spring Chinook Salmon, Snake River Summer Steelhead, Bull Trout, Lamprey, etc..."
			})

class prospectus_step_8(forms.ModelForm):
	class Meta:
		model = Prospectus
		fields = ['project_description', 'project_objectives']
		labels = {
			'project_description': 'Project Description - Describe the current condition of the project area and the goal(s) of the proposed restoration activities.',
			'project_objectives': 'Project Objectives - Objectives should be S.M.A.R.T (Specific, Measurable, Achievable, Relevant, Time Bound) and be associated with accomplishing the goal(s) identified above.',
		}
	def __init__(self, *args, **kwargs):
		super(prospectus_step_8, self).__init__(*args, **kwargs)
		self.fields['project_description'].widget = forms.Textarea(attrs={
			'placeholder': "Project Description"
			})
		self.fields['project_objectives'].widget = forms.Textarea(attrs={
			'placeholder': "Project Objective"
			})

class prospectus_step_9(forms.ModelForm):
	class Meta:
		model = Prospectus
		fields = ['major_risks']
		labels = {
			'major_risks': 'Major Risks - Opportunity Lead should review the Feasibility Matrix with the Implementation Team as soon as possible to discuss risks and concerns identified.',
		}
	def __init__(self, *args, **kwargs):
		super(prospectus_step_9, self).__init__(*args, **kwargs)
		self.fields['major_risks'].widget = forms.Textarea(attrs={
			'placeholder': "Briefly describe major barriers to implementation and the approach you will use to resolve them."
			})

class prospectus_step_10(forms.ModelForm):
	class Meta:
		model = Prospectus
		fields = ['permits_consultations']
		labels = {
			'permits_consultations': 'Permits & Consultations - Check all that apply'
		}
		widgets = {
			'permits_consultations': forms.CheckboxSelectMultiple()
		}

	def __init__ (self, *args, **kwargs):
		super(prospectus_step_10, self).__init__(*args, **kwargs)
		self.fields['permits_consultations'].empty_label = None

class prospectus_step_11(forms.ModelForm):
	class Meta:
		model = Prospectus
		fields = ['anticipated_year', 'monitoring']
		labels = {
			'anticipated_year': 'Anticipated Implementation Year',
			'monitoring': 'Monitoring',
		}
	def __init__ (self, *args, **kwargs):
		super(prospectus_step_11, self).__init__(*args, **kwargs)
		self.fields['anticipated_year'].widget = forms.TextInput(attrs={
			'placeholder': "Year"
			})
		self.fields['monitoring'].widget = forms.Textarea(attrs={
			'placeholder': "Briefly describe the scale and scope of anticipated monitoring"
			})

class prospectus_step_12(forms.ModelForm):
	class Meta:
		model = Prospectus
		fields = ['multi_phase', 'multi_phase_desc', 'ph1_standalone', 'phase_approach_value_loss']
		labels = {
			'multi_phase': 'Is this project part of a multi-phase effort?',
			'multi_phase_desc': 'If yes, please briefly describe the phases',
			'ph1_standalone': 'If this project is a multi-phase effort, can Phase 1 be a stand alone project?',
			'phase_approach_value_loss': 'How is restoration value affected by phased approach and potential loss of future phases?'
		}
	def __init__ (self, *args, **kwargs):
		super(prospectus_step_12, self).__init__(*args, **kwargs)
		self.fields['multi_phase_desc'].widget = forms.Textarea(attrs={
			'placeholder': "Briefly describe each phase"
			})
		self.fields['phase_approach_value_loss'].widget = forms.Textarea(attrs={
			'placeholder': "Briefly describe your answer"
			})

class prospectus_step_13(forms.ModelForm):
	class Meta:
		model = Prospectus
		fields = ['project_cost', 'bpa_funding', 'fip_funding', 'grmw_design_funds']
		labels = {
			'project_cost': 'Estimated Total Project Cost',
			'bpa_funding': 'Requested BPA Funding',
			'fip_funding': 'Requested OWEB FIP Funding',
			'grmw_design_funds': "Are design funds being requested from GRMW as part of this prospectus? If you select 'No', you are done and you will be redirected to the stepwise dashboard."
		}
	def __init__ (self, *args, **kwargs):
		super(prospectus_step_13, self).__init__(*args, **kwargs)
		self.fields['project_cost'].widget = forms.TextInput(attrs={
			'placeholder': "Total Project Cost"
			})
		self.fields['bpa_funding'].widget = forms.TextInput(attrs={
			'placeholder': "BPA Funding"
			})
		self.fields['fip_funding'].widget = forms.TextInput(attrs={
			'placeholder': "OWEB FIP Funding"
			})

	def clean_grmw_design_funds(self):
		design_funds = self.cleaned_data.get('grmw_design_funds')
		if(design_funds == None):
			raise forms.ValidationError("You must select either 'Yes' or 'No'.")
		return design_funds

class prospectus_step_14(forms.ModelForm):
	class Meta:
		model = Prospectus
		fields = ['funds_request_option']
		labels = {
			'funds_request_option': mark_safe('Design Fund Request<br/><br/>Please Select an Option<br/><br/>Option 1: BPA works directly with Sponsor/Opportunity Lead (OL) to create a Statement of Work (SOW) for engineering services for a specific project.  Technical assistance from Civil Engineer can be requested by OL to develop SOW.  BPA would contract directly with the consultant via BPA’s pre-qualified consultants list (QVL) and manage the contract.  The contract would include provisions that include the required coordination and integration with the OL during the life of the contract.<br/><br/>Option 2:  With assistance from BPA, OL develops a SOW for engineering services for a specific project then advertises for consultant services.  Once a selection is made BPA would contract directly with consultant and manage the contract.  The contract would include provisions that include the required coordination and integration with the OL during the life of the contract. This is consistent with the current process for BPA’s implementation contracting and similar to the process that USBR uses in their tributary habitat contracting with improvements (i.e. OL collaboration in SOW development).')
		}

	def clean_funds_request_option(self):
		funds_option = self.cleaned_data.get('funds_request_option')
		if(funds_option == None):
			raise forms.ValidationError("You must select either 'Option 1' or 'Option 2'.")
		return funds_option

class prospectus_step_15(forms.ModelForm):
	class Meta:
		model = Prospectus
		fields = ['work_type', 'work_specialties']
		labels = {
			'work_type': 'What Type of Work is Needed? - Check all that apply',
			'work_specialties': mark_safe("<br/><br/>What Specialties are Needed? - Check all that apply"),
		}
		widgets = {
			'work_type': forms.CheckboxSelectMultiple(),
			'work_specialties': forms.CheckboxSelectMultiple(),
		}

	def __init__ (self, *args, **kwargs):
		super(prospectus_step_15, self).__init__(*args, **kwargs)
		self.fields['work_type'].empty_label = None
		self.fields['work_specialties'].empty_label = None

class stepwise_comment_form(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['subject', 'content', 'attachment']
		labels = {
			'subject': 'Subject',
			'content': 'Reply',
			'attachment': 'Upload Attachment',
		}

	def clean_attachment(self):
		value = self.cleaned_data.get('attachment')
		if value != None:
			ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
			valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
			if not ext.lower() in valid_extensions:
				raise forms.ValidationError(u'Unsupported file extension. Allowed extensions are: .pdf, .doc, .docx, .jpg, .png, .xlsx, and .xls')
		return value

	def __init__ (self, *args, **kwargs):
		super(stepwise_comment_form, self).__init__(*args, **kwargs)
		self.fields['subject'].widget = forms.TextInput(attrs={
			'placeholder': "Subject"
			})
		self.fields['content'].widget = forms.Textarea(attrs={
			'placeholder': "Write a reply here..."
			})

class upload_draft_form(forms.ModelForm):
	class Meta:
		model = Draft
		fields = [
			'draft_file'
		]
		labels = {
			'draft_file': 'Upload Draft',
		}

	def clean_draft_file(self):
		value = self.cleaned_data.get('draft_file')
		if value != None:
			ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
			valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
			if not ext.lower() in valid_extensions:
				raise forms.ValidationError(u'Unsupported file extension. Allowed extensions are: .pdf, .doc, .docx, .jpg, .png, .xlsx, and .xls')
		return value

class upload_final_form(forms.ModelForm):
	class Meta:
		model = Proposal
		fields = [
			'proposal_file'
		]
		labels = {
			'proposal_file': 'Upload Final'
		}

	def clean_proposal_file(self):
		value = self.cleaned_data.get('proposal_file')
		if value != None:
			ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
			valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
			if not ext.lower() in valid_extensions:
				raise forms.ValidationError(u'Unsupported file extension. Allowed extensions are: .pdf, .doc, .docx, .jpg, .png, .xlsx, and .xls')
		return value
