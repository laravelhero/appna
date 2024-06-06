from django.urls import path
from . import views

urlpatterns = [    
    path('', views.Member.as_view(), name="member"),
    path('donation/', views.Donation.as_view(), name="donation"),
]
