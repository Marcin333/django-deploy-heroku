from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views  import ProductDetailView, ProductListView, VariationListView, WishListView

urlpatterns = [
        # url(r'^(?P<id>\d+)', 'products.views.get_product_detail_view', name='get_product_detail_view'),
        url(r'^$', ProductListView.as_view(), name='products'),
        url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
        url(r'^(?P<pk>\d+)/inventory/$', VariationListView.as_view(), name='product_inventory'),
        url(r'^wishlist/$', WishListView.as_view(), name='wishlist'),
]
# url(r'^wishlist/$', 'views.wishlist', name='wishlist'),