from django.urls import path
from . import views

urlpatterns = [
    path('create_checkout_session/', views.create_checkout_session, name='create_checkout_session'),
]
