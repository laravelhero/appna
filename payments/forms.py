from paypal.standard.forms import PayPalPaymentsForm
from django.utils.safestring import mark_safe

class DonationPayPalPaymentsForm(PayPalPaymentsForm):

    def get_html_submit_element(self):
        return mark_safe("""<button type="submit">Continue on PayPal website</button>""")

class MemberPayPalPaymentsForm(PayPalPaymentsForm):

    def get_html_submit_element(self):
        return mark_safe("""<button type="submit">Pay</button>""")