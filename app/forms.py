from django import forms 
from .models import Donation, Member 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field, Row, Column

class DonationForm(forms.ModelForm): 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('purpose', css_class='form-group col-md-6 mb-0'),
                Column('amount', css_class='form-group col-md-4 mb-0'),
            ),
            Submit('submit', 'Sign in here')
        )

        
    class Meta:
        model = Donation
        fields = '__all__'       
        

class MemberForm(forms.ModelForm): 
    class Meta:
        model = Member
        fields = '__all__'