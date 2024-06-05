from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
import uuid 

from app.forms import DonationForm, MemberForm
from payments.forms import MemberPayPalPaymentsForm, DonationPayPalPaymentsForm


def checkout(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'donation':
            amount = request.POST.get('amount')
            form = DonationForm(request.POST)
            item_name = 'Donation'

        else:
            amount = request.POST.get('amount')
            form = MemberForm(request.POST, request.FILES)
            item_name = 'Membership'

        paypal_dict = {
            "business": "sb-oso3c31035489@business.example.com",
            "amount": amount,
            "currency_code": 'USD',
            "item_name": item_name,
            "invoice": f'{uuid.uuid4()}-{uuid.uuid4()}',
            "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
            "return": request.build_absolute_uri(reverse('payments:payment_success')),
            "cancel_return": request.build_absolute_uri(reverse('payments:payment_fail')),
        }
     
        if form.is_valid():
            request.session['form'] = form.cleaned_data
            request.session['form_type'] = form_type

            # if form_type == 'donation':
            #     paypal_form = DonationPayPalPaymentsForm(initial=paypal_dict)
            # else:
            #     paypal_form = MemberPayPalPaymentsForm(initial=paypal_dict)

            # context = {
            #     "paypal_form": paypal_form,
            #     "amount": amount,
            #     "form": form,
            #     "form_type": form_type,
            # }

            # return render(request, 'payments/checkout.html', context)
            return redirect('payments:payment_success')

        if form_type == 'donation':
            template = 'app/donation.html'
        else:
            template = 'app/member.html'

        return render(request, template, {'form': form, 'form_type': form_type})

    return render(request, 'app/checkout.html')

def payment_success(request):
    if request.method == 'GET' and 'form' in request.session:
        if(request.session['form_type']=='donation'):
            form_data = request.session['form']
            form = DonationForm(form_data)
            form.save()
        elif request.session['form_type']=='member':
            form_data = request.session['form']
            form = MemberForm(form_data)
    
            User.objects.create_user(username=form_data.get('email'), password=form_data.get('password'), is_staff=True, is_active=True)
            form.save()

        del request.session['form']
        del request.session['form_type']
    return render(request, 'payments/payment-success.html') 

def payment_fail(request):
    del request.session['form']
    del request.session['form_type']
    return render(request, 'payments/payment-fail.html') 




