from django.contrib import admin
from .models import UserCheckout, UserAddress, Order

class UserCheckoutAdmin(admin.ModelAdmin):
	list_display = ['id', 'email']

	class Meta:
		model = UserCheckout

admin.site.register(UserCheckout, UserCheckoutAdmin)
admin.site.register(UserAddress)
admin.site.register(Order)
