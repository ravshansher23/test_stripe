from django.conf import settings # new
from django.views.generic import TemplateView
from django.shortcuts import redirect
import stripe
from mainapp import models as mainapp_models
from django.urls import reverse
from django.views import View
from django.http import JsonResponse


stripe.api_key = settings.STRIPE_SECRET_KEY


class MainPageView(TemplateView):
    template_name = "mainapp/checkout.html"
    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context["items"] = mainapp_models.Item.objects.all()
        return context


class CreateCheckoutSessionView(View):
    
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = 'http://localhost:8000'
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': 'price_1Mb43CJLtPVKs6Q3S2qafBuc',
                        'quantity': 1,
                    },
                ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        print(checkout_session.url)
        return redirect(checkout_session.url, code=303)

class SuccessView(TemplateView):
    template_name = "mainapp/success.html"        

class CancelledView(TemplateView):
    template_name = "mainapp/cancelled.html"        