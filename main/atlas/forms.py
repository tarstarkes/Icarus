#forms.py
from django import forms
from atlas.models import *
import re
from django.utils.safestring import mark_safe

class atlas_bsr_form(forms.ModelForm):
	class Meta:
		model = atlas_bsr
		fields = [
		'name',
		'desc',
		'geomorphic_potential',
		'current_habitat_cond',
		'current_temp',
		'future_cond',
		'tier_id',
		]

class bsr_comment_form(forms.ModelForm):
	class Meta:
		model = bsr_comment
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
		super(bsr_comment_form, self).__init__(*args, **kwargs)
		self.fields['subject'].widget = forms.TextInput(attrs={
			'placeholder': "Subject"
			})
		self.fields['content'].widget = forms.Textarea(attrs={
			'placeholder': "Write a reply here..."
			})

class bsr_tier_form(forms.ModelForm):
	class Meta:
		model = atlas_bsr
		fields = ["tier_id",]
		
class opportunity_form(forms.ModelForm):
	class Meta:
		model = bsr_opportunity
		fields = ['location']
		labels = {
			'location': 'location',
		}

class periodicity_life_stage_form(forms.ModelForm):
	class Meta:
		model = life_stage
		fields = ['species', 'life_stage_name']

class utilization_form(forms.ModelForm):
	class Meta:
		model = utilization
		exclude = ['bsr_id']
		widget = {'comment': forms.Textarea(attrs={'resize':'none'})}

class utilization_score_form(forms.ModelForm):
	class Meta:
		model = utilization_score
		fields = "__all__"

class limiting_factor_form(forms.ModelForm):
	class Meta:
		model = limiting_factor_instance
		fields =["limiting_factor_id", "comment"]

class limiting_factor_score_form(forms.ModelForm):
	class Meta:
		model = limiting_factor_score
		fields = "__all__"

class new_opportunity_form(forms.ModelForm):
	class Meta:
		model = bsr_opportunity
		fields = ["opportunity_name", "description", "status"]

class opp_map(forms.ModelForm):
	class Meta:
		model = bsr_opportunity
		fields = ["location", "zoom", "center"]

class opp_action_form(forms.ModelForm):
	class Meta:
		model= bsr_opportunity_action
		fields = ['action_id',]
		labels = {
			'action_id': 'Resoration Action'
		}

class opp_np_form(forms.ModelForm):
	class Meta:
		model = bsr_opportunity
		fields = ["natural_process",]

class opp_water_form(forms.ModelForm):
	class Meta:
		model = bsr_opportunity
		fields = ["water_right_date", "water_flow_rate"]

class opp_fc_form(forms.ModelForm):
	class Meta:
		model= bsr_opportunity
		fields = [
		"fc_landowner_willingness", 
		"fc_design_effort",
		"fc_constuction_effort",
		"fc_site_access_effort",
		"fc_sm_dewatering_erosion_ctrl_effort",
		"fc_risk_goal_objectives",
		"fc_risk_public_safety",
		"fc_regulatory_requirements",
		"fc_value",
		]

class rest_action_form(forms.ModelForm):
	class Meta:
		model = restoration_actions_score
		fields = "__all__"

class opp_comment_form(forms.ModelForm):
	class Meta:
		model = bsr_opportunity
		fields = ["comments",]

class opp_desc_form(forms.ModelForm):
	class Meta:
		model = bsr_opportunity
		fields = ["description",]