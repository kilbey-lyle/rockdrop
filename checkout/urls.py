from django.urls import path
from . import views

urlpatterns = [
    path('create_checkout_session/', views.create_checkout_session, name='create_checkout_session'),
    path('checkout_success/', views.checkout_success, name='checkout_success'),
]
