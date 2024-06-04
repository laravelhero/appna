from django.urls import path

from payments import views


app_name = 'payments'
urlpatterns = [
    path('checkout', views.checkout, name='checkout'),
    path('payment-success', views.payment_success, name='payment_success'),
    path('payment-fail', views.payment_fail, name='payment_fail'),

]