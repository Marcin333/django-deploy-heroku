from __future__ import absolute_import
from django import forms
from django.contrib.auth import get_user_model
from .models import UserAddress
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import (
    AppendedText, PrependedText, PrependedAppendedText, FormActions, Field, Div)
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Button
User = get_user_model()

class GuestCheckoutForm(forms.Form):
	email = forms.EmailField()
	email2 = forms.EmailField(label='Verify Email')

	def clean_email2(self):
		email = self.cleaned_data.get("email")
		email2 = self.cleaned_data.get("email2")

		if email == email2:
			user_exists = User.objects.filter(email=email).count()
			if user_exists != 0:
				raise forms.ValidationError("This User already exists. Please login instead.")
			return email2
		else:
			raise forms.ValidationError("Please confirm emails are the same")

class AddressForm(forms.Form):
	billing_address = forms.ModelChoiceField(
			queryset=UserAddress.objects.filter(type="billing"),
			widget = forms.RadioSelect,
			empty_label = None
			)
	shipping_address = forms.ModelChoiceField(
		queryset=UserAddress.objects.filter(type="shipping"),
		widget = forms.RadioSelect,
		empty_label = None,

		)
	
class UserAddressForm(forms.ModelForm):
	# default = forms.BooleanField(label='Select if the shipping address is the some', required=False)
# 	# address = forms.CharField(label='Address', required=True)
# 	# address2 = forms.CharField(label='Second Address', required=False) #help_text='Hello'

	def __init__(self, *args, **kwargs):
	    super(UserAddressForm, self).__init__(*args, **kwargs)
	    self.helper = FormHelper(self)
	    self.helper.form_method = 'POST'
	    self.helper.form_class = 'form-horizontal'
	    self.helper.label_class = 'col-lg-2 col-md-2 col-sm-2 col-xs-10 col-xs-offset-1 col-sm-offset-0'
	    self.helper.field_class = 'col-lg-9 col-md-9 col-sm-9 col-xs-10 col-xs-offset-1 col-sm-offset-0'
	    self.helper.form_error_title = 'Sorry, input is not correct'
	    self.helper.html5_required = True
	    self.helper.layout = Layout(	    	
	        Field('street', placeholder='Street', css_class='calendar'),
	        Field('city', placeholder='City'),
	        Field('state', placeholder='State'),
	        Field('country', placeholder='Country'), 
	        Field('post_code', placeholder='Post Code'),
	        Field('phone', placeholder='Phone number'),
	        Field('type'),
            Submit('submit', 'Submit', css_class='btn btn-warning btn-lg') 
  				
	    	)
	class Meta:
		model = UserAddress
		fields = [
			"street",
			"city",
			"state",
			"post_code",
			"country",
			"phone",
			"type"
			
		]