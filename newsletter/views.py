import json
from django.shortcuts import render, redirect
from .forms import ContactUsForm, ContactForm, NewsletterForm
from django.core.mail import send_mail
from django.http import HttpResponseBadRequest, JsonResponse
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
from .models import ContactUs,  Condition, Newsletter
from products.models import ProductFeatured, Product

def home(request):
	message = 'Welcome'
	form = ContactForm(request.POST or None)
	featured_image = ProductFeatured.objects.first()
	products = Product.objects.all().order_by('?')
	products2 = Product.objects.all().order_by('?')[:4]
	context = {'message': message, 'form':form, 'featured_image': featured_image, \
	'products': products, 'products2': products2}
	if form.is_valid():
		instance = form.save(commit=False)
		if not instance.full_name:
			full_name = 'Anonymous user'
			instance.full_name = full_name
		# if not instance.full_name:
		# 	instance.full_name = 'Anonymous user'
		instance.save()
		message = 'Thank you for sign up!'
		context = {'message': message}
	# if request.user.is_authenticated() and request.user.is_staff:
	# 	message = 'Hi {0}'.format(request.user)
	# 	emails = SignUp.objects.all().order_by('-timestamp')  #.filter(full_name__iexact='Anonymous user')
	# 	message2 = 'Hi staff!!'
	# 	context = { 'message2': message2}
	return render(request, 'home.html', context)

def contact(request):
	title = 'Contact Us'
	text_align_center = False
	form = ContactUsForm(request.POST or None)
	if form.is_valid():
		form_instance = form.save(commit=False)
		form_instance.save()
		messages.success(request, 'Thank you for message. We answer your question as soon as possible')
		return redirect('home')
	context = {'form': form, 'title': title}
	return render(request, 'contact.html', context)

# hello@teamcfe.com

def terms_and_conditions(request, slug):
	condition_text = Condition.objects.get(slug=slug)
	template = 'terms&Conditions/term_&_conditions.html'
	return render(request, template, {'condition_text': condition_text})

def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDER_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip


def newsletter(request):
	form = NewsletterForm(request.POST or None)
	# try:
	# 	x_forward = request.META.get("HTTP_X_FORWARDER_FOR")
	# 	if x_forward:
	# 	    ip = x_forward.split(",")[0]
	# 	else:
	# 	    ip = request.META.get("REMOTE_ADDR")
	# except:
	# 	ip = ""
	data = {}
	if form.is_valid():
		email = form.cleaned_data.get('email')
		new_subscriber, created = Newsletter.objects.get_or_create(email=email)
		# if not request.is_ajax():
		# 	print True
		if created:
			data['message'] = 'Thank You For Signing Up!'
			return JsonResponse(data)
		else:
			data['message'] = 'You have are already signed up'
			return JsonResponse(data)
	else:
		return HttpResponseBadRequest(json.dumps(form.errors), content_type='application/json' )


# # for key, val in form.cleaned_data.iteritems():
# 		# 	print key, val
# 		full_name = form.cleaned_data.get('full_name')
# 		email = form.cleaned_data.get('email')
# 		form_message = form.cleaned_data.get('message')
# 		subject = 'Django website.'
# 		# message = 'Thanks {0} for join in'.format(full_name)
# 		text_message = render_to_string('email_messages/confirmation_contact.txt')
# 		# html_message = render_to_string('email_messages/confirmation_contact.html')
# 		send_from = settings.EMAIL_HOST_USER
# 		send_to = email
# 		send_mail(subject, text_message, send_from, send_to, fail_silently=False)