from django.urls import path
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('payments/', views.payments, name='payments'),
    path('order_complete/', views.order_complete, name='order_complete'),
    #**************************
    path('payment_success/', views.payment_success, name='payment_success'),
    #**********************
    #**********************************
    path('payment-failed/', views.payment_unsuccessful, name='payment_unsuccessful'),

    #*********************************
]
