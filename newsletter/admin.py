from django.contrib import admin
from .forms import ContactUsForm, NewsletterForm
from .models import ContactUs, Condition, Newsletter

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "message", "timestamp", "updated"]
	form = ContactUsForm

class ConditionAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

	class Meta:
		model = Condition

class NewsletterAdmin(admin.ModelAdmin):
	list_display = ["email", 'timestamp']
	form = NewsletterForm

	class Meta:
		model = Newsletter

admin.site.register(ContactUs, SignUpAdmin)
admin.site.register(Condition, ConditionAdmin)
admin.site.register(Newsletter, NewsletterAdmin)