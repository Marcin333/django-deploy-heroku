from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages
from django.db.models import Q
from django.http import Http404, JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import Product, Variation, Category, Wish, WishItem
from .forms import VariationInventoryFormSet
from .mixins import StaffRequiredMixin, LoginRequiredMixin

class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'products/product_list.html'

class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
        obj = self.get_object() # This geting instance which coming through
        product_set = obj.product_set.all()  # This is first product
        default_products = obj.default_category.all()
        products = (product_set | default_products).distinct()
        context['products'] = products
        return context

class VariationListView(LoginRequiredMixin, ListView):
    model = Variation
    queryset = Variation.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(VariationListView, self).get_context_data(*args, **kwargs)
        context['formset'] = VariationInventoryFormSet(queryset=self.get_queryset())
        return context

    def get_queryset(self, *args, **kwargs):
        product_pk = self.kwargs.get('pk')
        if product_pk:
            product = get_object_or_404(Product, pk=product_pk)
            queryset = Variation.objects.filter(product=product)
        return queryset

    def post(self, request, *args, **kwargs):
        # print request.POST
        formset = VariationInventoryFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save(commit=False)
            for form in formset:
                new_item = form.save(commit=False)
                product_pk = self.kwargs.get('pk')
                product = get_object_or_404(Product, pk=product_pk)
                new_item.product = product
                new_item.save()
            messages.success(request, "Your inventory and pricing has been updated")
            return redirect('products')
        raise Http404


class ProductListView(ListView):
    model = Product
    # queryset = Product.objects.filter(active=True)

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context['now'] = timezone.now()
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            qs = self.model.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
            )
            try:
                qs2 = self.model.objects.filter(
                Q(price=query)
                )
                qs = (qs | qs2).distinct() # distinct() insure that model not give two objects
            except:
                pass
        return qs

import random
class ProductDetailView(DetailView):
    model = Product
    # template_name = <appname>/<modelname_detail.html
    # template_name = "product.html"
    def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		instance = self.get_object()
		context["related"] = sorted(Product.objects.get_related(instance), key=lambda x: random.random())[:6]    #.order_by("?")[:6] # ? = random ordering
		return context                                                 # key= lambda x: x.id, reverse=True == ['-title']

def get_product_detail_view(request, id):
    # product = Product.objects.get(id=id)
    product = get_object_or_404(Product, id=id)
    # try:
    #     product = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    template = 'products/product_detail.html'
    context = {'product':product}
    return render(request, template, context)

class WishListView(LoginRequiredMixin, View):
    model = Wish
    template_name = 'products/wishlist.html'

    def get_object(self, *args, **kwargs):
        wish_id = self.request.session.get('wish_id')
        if wish_id == None:
            wish = Wish()
            wish.save()
            wish_id = wish.id
            self.request.session['wish_id'] = wish_id
        wish = Wish.objects.get(id=wish_id)
        if self.request.user.is_authenticated():
            wish.user = self.request.user
            wish.save()
        return wish

    def get(self, request, *args, **kwargs):
        wish = self.get_object()
        item_id = request.GET.get('item')
        item_added = False
        flush_message = ""
        if item_id:
            item_instance = get_object_or_404(Variation, id=item_id)
            wish_list, created = WishItem.objects.get_or_create(wish=wish, item=item_instance)
            if created:
                flush_message = "Item added to the wishlist"
                item_added = True
                wish_list.save()
            else:
                flush_message = "Item has been updated"
                item_added = False
            if not request.is_ajax():
                return HttpResponseRedirect(reverse('wishlist'))
        if request.is_ajax():
            data = {"item_added":item_added, "flush_message": flush_message}
            return JsonResponse(data)
        context = {'object': self.get_object()}
        template = self.template_name
        return render(request, template, context)


# def wishlist(request):
#     var_id = request.GET.get('item')
#     variation = Variation.objects.get(id=int(var_id))
#     wish = Wish()
#     wish.user = request.user
#     wish.save()
#     wish_item = WishItem.objects.get_or_create(wish=wish, item=variation)[0]
#     wish_item.save()
#     all_items = wish_item.wish.items.all()
#     print wish_item
#     return render(request, 'products/wishlist.html',
#                                  {'wish':wish, 
#                                   'wish_item': wish_item, 
#                                   'all_items': all_items})
