from django.urls import path
from django.views.decorators.cache import cache_page
from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main_page"),
    path('create-checkout-session/', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path("buy/<int:pk>", views.BuyView.as_view(), name="buy"),
    path("item/<int:pk>", views.ItemView.as_view(), name="item"),
    path("success/", views.SuccessView.as_view(), name="success"),
    path("cancel/", views.CancelledView.as_view(), name="cancelled"),
]