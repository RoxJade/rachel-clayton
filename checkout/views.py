from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Iz0uBKgP7mMfw1vw7e4vNw6jbYtMGceFKmZQPBGJGu47zvWTl2GUEZTlXSMr8eZdlsVfwciPMU22Wp5d3dVS9Vm00r4OeTRWE',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
