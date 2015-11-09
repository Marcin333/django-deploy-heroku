from django.db import models
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe 

class ContactUs(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.email

class Condition(models.Model):
	title = models.CharField(max_length=50, null=True, blank=True)
	text_field = models.TextField()
	slug = models.SlugField(unique=True)

	def __unicode__(self):
		return self.title

	def display_my_safe_field(self):
		return mark_safe(self.text_field)

	def get_absolute_url(self):
		return reverse('condition', kwargs={'slug':self.slug})

class Newsletter(models.Model):
	email = models.EmailField()
	# user_ip = models.CharField(max_length=120, default="ABC")
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.email

	class Meta:
		ordering = ['-timestamp']