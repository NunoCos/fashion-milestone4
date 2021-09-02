from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There are no items in your bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JVDT0IlsYuUxYfDXZdD97HOag8kMfjXjMYJXPAKWih6YaQhL1s7piOmd0XLcOif7OjzUNeAEjfnP0pnSz4Hj9qA00qCZ8piUd',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)