import uuid
from django import template
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm

register = template.Library()


# Paypal subscriptions
def paypal_form_for(product, user):
    if user.is_customer(product):
        html = "You're a customer!"

    else:
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "currency_code": "EUR",
            "cmd": "_xclick-subscriptions",
            "a3": product.price,
            "p3":1,
            "t3":"M",
            "src":1,
            "Sra":1,
            "item_name": product.name,
            "invoice": uuid.uuid4(),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return" % settings.SITE_URL,
            "cancel_return":"%s/paypal-cancel" % settings.SITE_URL,
            "custom": "%s-%s" % (product.pk, user.id),
        }

        if settings.DEBUG:
            html = PayPalPaymentsForm(initial=paypal_dict, button_type='subscribe').sandbox()
        else:
            html = PayPalPaymentsForm(initial=paypal_dict, button_type='subscribe').render()
    return html

register.simple_tag(paypal_form_for)
