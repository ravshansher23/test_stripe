from django.conf import settings  # new
from django.views.generic import TemplateView
from django.shortcuts import redirect, get_object_or_404
import stripe
from mainapp import models as mainapp_models
from mainapp import forms as mainapp_forms
from django.views import View
from django.http import HttpResponse
stripe.api_key = settings.STRIPE_SECRET_KEY


class MainPageView(TemplateView):
    template_name = "mainapp/checkout.html"

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context["items"] = mainapp_models.Item.objects.all()
        context["form"] = mainapp_forms.AddressForm()
        return context


class CreateCheckoutSessionView(View):

    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = 'http://localhost:8000'
        if request.POST.get("item"):
            checkout_session = stripe.checkout.Session.create(
                customer_email=request.POST.get("email"),
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': request.POST.get("item"),
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + '/success/',
                cancel_url=YOUR_DOMAIN + '/cancel/',
            )
            print(checkout_session.url)
            return redirect(checkout_session.url, code=303)


class BuyView(View):
    def get(self, request, pk=None, *args, **kwargs):
        YOUR_DOMAIN = 'http://localhost:8000'
        item = get_object_or_404(mainapp_models.Item, pk=pk)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': item.key,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )

        return HttpResponse(checkout_session.stripe_id)

    def post(self, request, pk=None, *args, **kwargs):
        YOUR_DOMAIN = 'http://localhost:8000'
        item = get_object_or_404(mainapp_models.Item, pk=pk)
        print(item.key)
        checkout_session = stripe.checkout.Session.create(
            customer_email=request.POST.get("email"),
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': item.key,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        print(checkout_session.url)
        return redirect(checkout_session.url, code=303)


class ItemView(TemplateView):
    template_name = "mainapp/item.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super(ItemView, self).get_context_data(**kwargs)
        context["items"] = get_object_or_404(mainapp_models.Item, pk=pk)
        context["form"] = mainapp_forms.ItemForm()
        return context


class SuccessView(TemplateView):
    template_name = "mainapp/success.html"


class CancelledView(TemplateView):
    template_name = "mainapp/cancelled.html"
