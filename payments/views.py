from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
import uuid

from app.forms import DonationForm, MemberForm
from app.models import Member, Donation
from payments.forms import MemberPayPalPaymentsForm, DonationPayPalPaymentsForm


def checkout(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        amount = request.POST.get('amount')

        # Prepare PayPal dictionary
        paypal_dict = {
            "business": "sb-oso3c31035489@business.example.com",
            "amount": amount,
            "currency_code": 'USD',
            "item_name": 'Donation' if form_type == 'donation' else 'Membership',
            "invoice": f'{uuid.uuid4()}-{uuid.uuid4()}',
            "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
            "return": request.build_absolute_uri(reverse('payments:payment_success')),
            "cancel_return": request.build_absolute_uri(reverse('payments:payment_fail')),
        }

        # Initialize the correct form based on form_type
        if form_type == 'donation':
            form = DonationForm(request.POST)
        else:
            form = MemberForm(request.POST, request.FILES)

        if form.is_valid():
            if form_type == 'donation':
                donation = form.save()
                request.session['donation_id'] = donation.id
                request.session['form_type'] = 'donation'
                paypal_form = DonationPayPalPaymentsForm(initial=paypal_dict)
            else:
                form.instance.is_paid = True
                member = form.save()
                user = User.objects.create_user(
                    username=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                    is_staff=True,
                    is_active=True
                )
                request.session['member_id'] = member.id
                request.session['user_id'] = user.id
                request.session['form_type'] = 'member'
                paypal_form = MemberPayPalPaymentsForm(initial=paypal_dict)

            context = {
                "paypal_form": paypal_form,
                "amount": amount,
            }
            return render(request, 'payments/checkout.html', context)

        # If form is not valid, render the appropriate template with form errors
        template = 'app/donation.html' if form_type == 'donation' else 'app/member.html'
        return render(request, template, {'form': form, 'form_type': form_type})

    # If request method is GET, render the default checkout page
    return render(request, 'app/checkout.html')


def payment_success(request):
    request.session.flush()  # Clears all session data
    return render(request, 'payments/payment-success.html')


def payment_fail(request):
    form_type = request.session.get('form_type')

    if form_type == 'member':
        member_id = request.session.get('member_id')
        user_id = request.session.get('user_id')
        if member_id and user_id:
            Member.objects.filter(id=member_id).delete()
            User.objects.filter(id=user_id).delete()
    else:
        
        donation_id = request.session.get('donation_id')
        print('----------------------------------------')
        print(donation_id)
        if donation_id:
            Donation.objects.filter(id=donation_id).delete()

    request.session.flush()  # Clears all session data
    return render(request, 'payments/payment-fail.html')
