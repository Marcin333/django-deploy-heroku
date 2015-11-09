from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, FormView, View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.http import Http404
from django.conf import settings
from django.template import Context, Template
# get_template is what we need for loading up the template for parsing.
from django.template.loader import get_template
# Create your views here.

from .forms import AddressForm, UserAddressForm
from .models import UserAddress, UserCheckout, Order
from .mixins import CartOrderMixin, LoginMixinRequired

import braintree

if settings.DEBUG:
    braintree.Configuration.configure(braintree.Environment.Sandbox,
        merchant_id=settings.BRAINTREE_MERCHANT_ID,
        public_key=settings.BRAINTREE_PUBLIC,
        private_key=settings.BRAINTREE_PRIVATE
    )


class OrderDetail(DetailView):
    model = Order

    def dispatch(self, request, *args, **kwargs):
        try:
            user_check_id = self.request.session.get('user_checkout_id')
            user_checkout = UserCheckout.objects.get(id=user_check_id)
        except UserCheckout.DoesNotExist:
            # user_checkout = UserCheckout.objects.get(user=request.user)
            user_checkout = request.user.usercheckout
            user_checkout = None
        
        obj = self.get_object()
        # print obj
        if obj.user == user_checkout and user_checkout is not None:
            return super(OrderDetail, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404


class UserAddressCreateView(CreateView):
    form_class = UserAddressForm
    template_name = "forms.html"
    success_url = "/checkout/address/"

    def get_checkout_user(self):
        user_check_id = self.request.session.get("user_checkout_id")
        user_checkout = UserCheckout.objects.get(id=user_check_id)
        return user_checkout

    def form_valid(self, form, *args, **kwargs):
        form.instance.user = self.get_checkout_user()
        default = form.cleaned_data.get("default")
        return super(UserAddressCreateView, self).form_valid(form, *args, **kwargs)


class AddressSelectFormView(CartOrderMixin, FormView):
    form_class = AddressForm
    template_name = "orders/address_select.html"


    def dispatch(self, *args, **kwargs):
        b_address, s_address = self.get_addresses()
        if b_address.count() == 0:
            messages.success(self.request, "Please add a billing address before continuing")
            return redirect("user_address_create")
        elif s_address.count() == 0:
            messages.success(self.request, "Please add a shipping address before continuing")
            return redirect("user_address_create")
        else:
            return super(AddressSelectFormView, self).dispatch(*args, **kwargs)


    def get_addresses(self, *args, **kwargs):
        user_check_id = self.request.session.get("user_checkout_id")
        user_checkout = UserCheckout.objects.get(id=user_check_id)
        b_address = UserAddress.objects.filter(
                user=user_checkout,
                type='billing',
            )
        s_address = UserAddress.objects.filter(
                user=user_checkout,
                type='shipping',
            )
        return b_address, s_address


    def get_form(self, *args, **kwargs):
        form = super(AddressSelectFormView, self).get_form(*args, **kwargs)
        b_address, s_address = self.get_addresses()
        form.fields["billing_address"].queryset = b_address
        form.fields["shipping_address"].queryset = s_address
        return form

    def form_valid(self, form, *args, **kwargs):
        billing_address = form.cleaned_data["billing_address"]
        shipping_address = form.cleaned_data["shipping_address"]

        # self.request.session["billing_address_id"] = billing_address.id
        # self.request.session["shipping_address_id"] = shipping_address.id
        order = self.get_order()
        order.billing_address = billing_address
        order.shipping_address = shipping_address
        order.save()
        return  super(AddressSelectFormView, self).form_valid(form, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        return "/checkout/"


class CheckoutFinalView(CartOrderMixin, View):

    def post(self, request, *args, **kwargs):
        order = self.get_order()
        user = order.user.email
        order_total = order.order_total
        post_code = order.billing_address.post_code
        nonce = self.request.POST.get('payment_method_nonce')
        if nonce:
            result = braintree.Transaction.sale({
                "amount": order_total,
                "payment_method_nonce": nonce,
                "billing": {
                    "postal_code": post_code
                },
                "options": {
                    "submit_for_settlement": True
                }
            })
            if result.is_success:
                order.mark_completed(order_id=result.transaction.id)
                messages.success(request, 'Thank you for your order.')
                order_id = request.session['order_id']
                subject = 'Ecommerce Django Site'
                # message = 'Thank You For Your Order. Your order id is %s'% request.session['order_id']
                text_message = render_to_string('message.txt')
                html_message = get_template('message.html').render(
                        Context({"order_id": order_id})
                    )
                send_from = settings.EMAIL_HOST_USER
                send_to = (user,)
                send_mail(subject, text_message, send_from, send_to, html_message=html_message, fail_silently=False)
                del request.session['order_id']
                del request.session['cart_id']
            else:
                messages.success(request, 'There was some problem with your order.')
                messages.success(request, '{0}'.format(result.message))
                return redirect('checkout_view')
        return redirect('order_detail', pk=order.pk)

    def get(self, request, *args, **kwargs): # must be. Otherwise it will be 405 error.
        return redirect('checkout_view')


class OrderList(LoginMixinRequired, ListView):
    queryset = Order.objects.all()

    def get_queryset(self):
        user_check_id = self.request.session.get("user_checkout_id")
        user_checkout = UserCheckout.objects.get(id=user_check_id)
        return super(OrderList, self).get_queryset().filter(user=user_check_id)