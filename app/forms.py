from django import forms 
from .models import * 
from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field,Layout, ButtonHolder, Submit

class DonationForm(forms.ModelForm): 
    class Meta:
        model = Donation
        fields = '__all__'

class MemberForm(forms.ModelForm): 
    class Meta:
        model = Member
        fields = '__all__'