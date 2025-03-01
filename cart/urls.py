from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('add_single_item_to_cart/<item_id>', views.add_single_item_to_cart, name='add_single_item_to_cart'),
    path('delete_an_item_from_cart/<item_id>', views.delete_an_item_from_cart, name='delete_an_item_from_cart'),

]
