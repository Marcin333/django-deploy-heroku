from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'views.home', name='home'),
    url(r'^terms/$', 'views.terms_and_conditions', name='condition'),
    

]
