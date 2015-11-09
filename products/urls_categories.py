from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views  import CategoryListView, CategoryDetailView

urlpatterns = [
        # url(r'^(?P<id>\d+)', 'products.views.get_product_detail_view', name='get_product_detail_view'),
        url(r'^$', CategoryListView.as_view(), name='category'),
        url(r'^(?P<slug>[\w-]+)/$', CategoryDetailView.as_view(), name='category_detail'),
]
