from .models import ContactUs, Newsletter
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import (
    AppendedText, PrependedText, PrependedAppendedText, FormActions, Field, Div)
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Button

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	massage = forms.CharField()

class ContactUsForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
	    super(ContactUsForm, self).__init__(*args, **kwargs)
	    self.helper = FormHelper(self)
	    self.helper.form_method = 'POST'
	    self.helper.form_class = 'form-horizontal'
	    self.helper.label_class = 'col-lg-2 col-md-2 col-sm-2 col-xs-10 col-xs-offset-1 col-sm-offset-0'
	    self.helper.field_class = 'col-lg-9 col-md-9 col-sm-9 col-xs-10 col-xs-offset-1 col-sm-offset-0'
	    self.helper.form_error_title = 'Sorry, input is not correct'
	    self.helper.html5_required = True
	    self.helper.layout = Layout(	    	
	        Field('full_name'),
	        Field('email'),
	        Field('message'),
            Submit('submit', 'Submit', css_class='btn btn-warning btn-lg') 
  				
	    	)
	class Meta:
		model = ContactUs
		fields = ['full_name', 'email', 'message']
		

class NewsletterForm(forms.ModelForm):
	class Meta:
		model = Newsletter
		fields = ['email']

	# def clean_email(self):
	# 	email = self.cleaned_data.get('email')
	# 	# email_base, provider = email.split("@")
	# 	# domain, extension = provider.split('.')
	# 	# if not domain == 'USC':
	# 	# 	raise forms.ValidationError("Please make sure you use your USC email.")
	# 	if not email[-3:] == "edu":
	# 		raise forms.ValidationError("Please use a valid .edu email address")
	# 	return email
