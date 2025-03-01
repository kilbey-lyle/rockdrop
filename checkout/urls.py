from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('create_checkout_session/', views.create_checkout_session, name='create_checkout_session'),
]
