from django.urls import path
from . import views

urlpatterns = [
    path('donation/', views.Donation.as_view(), name="donation"),
    path('member/', views.Member.as_view(), name="member"),
]
