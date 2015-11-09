from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from carts.views import CheckoutView
from orders.views import AddressSelectFormView, UserAddressCreateView, CheckoutFinalView

urlpatterns = [
	url(r'^$', CheckoutView.as_view(), name='checkout_view'),
    url(r'^address/$', AddressSelectFormView.as_view(), name='order_address'),
    url(r'^address/add/$', UserAddressCreateView.as_view(), name='user_address_create'),
    url(r'^final/$', CheckoutFinalView.as_view(), name='checkout_final'),
]