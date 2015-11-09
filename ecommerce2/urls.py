"""ecommerce2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from products.views import WishListView
from carts.views import CartView, CartCountView, CheckoutView 
from orders.views import AddressSelectFormView, UserAddressCreateView, CheckoutFinalView,\
        OrderList, OrderDetail

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^ajax/newsletter/$', 'newsletter.views.newsletter', name='ajax_newsletter'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^categories/', include('products.urls_categories')),
    url(r'^cart/$', CartView.as_view(), name='cart'),
    url(r'^orders/$', OrderList.as_view(), name='orders'),
    url(r'^orders/(?P<pk>\d*)/$', OrderDetail.as_view(), name='order_detail'),
    url(r'^cart/count$', CartCountView.as_view(), name='cart_items_count'),
    url(r'^checkout/', include('orders.urls')),
    # url(r'^conditions/', include('newsletter.urls')),
    url(r'^conditions/(?P<slug>[\w-]+)/$', 'newsletter.views.terms_and_conditions', name='condition'),
    
]   

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
