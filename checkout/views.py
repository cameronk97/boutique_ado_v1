import os

from django.contrib import messages
from django.shortcuts import redirect, render, reverse

from .forms import OrderForm


def checkout(request):

    stripe_public_key = os.environ.get('STRIPE_PUBLIC_KEY')
    client_secret = os.environ.get('CLIENT_SECRET')

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OMKwMJVGgq73B8SL9UX1qEDj9wagBIJn5sdol4ZXcGIRXbtVfmGStMNRMCZmd78J9N9Lzv4W8PZqPUbxPRMAlUa006avK83NJ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
