#forms.py
from django import forms
from home.models import *
import re
from django.utils.safestring import mark_safe

class add_subscriber(forms.ModelForm):
	class Meta:
		model = RipplesSubscribers
		fields = ['email', 'confirmation_key']

	def clean_email(self):
		value = self.cleaned_data['email']
		if value != None:
			print("dont forget about home/forms/")
			#raise forms.ValidationError(u'That is not a valid email, please enter a valid email address and try again.')
		return value

class ripples_form(forms.ModelForm):
	class Meta:
		model = Ripples
		fields = "__all__"
