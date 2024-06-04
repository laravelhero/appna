from django import forms 
from .models import Donation, Member 

class DonationForm(forms.ModelForm):        
    class Meta:
        model = Donation
        fields = '__all__'       
        

class MemberForm(forms.ModelForm): 
    class Meta:
        model = Member
        fields = '__all__'