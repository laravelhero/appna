from django.shortcuts import render, redirect
from . import forms
from . models import *
from django.views.generic import CreateView
from django.urls import reverse_lazy


class Donation(CreateView):
    model = Donation
    template_name = "donation.html"
    fields = "__all__"
    success_url = reverse_lazy('donation')

class Member(CreateView):
    model = Member
    template_name = "member.html"
    fields = "__all__"
    success_url = reverse_lazy('member')




