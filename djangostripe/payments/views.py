from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
import stripe
from .models import Item


def all_items(request):
    pass


def item(request, id):
    item = get_object_or_404(Item, id=id)
    template = 'item.html'
    api_key = settings.STRIPE_PUBLISHABLE_KEY
    context = {
        'item': item,
        'api_key': api_key
    }
    return render(request, template, context)        


@csrf_exempt
def buy(request, id):
    item = get_object_or_404(Item, pk=id)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                    'name': item.name,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url='https://tap-django-stripe.herokuapp.com',
        cancel_url='https://tap-django-stripe.herokuapp.com',
    )
    return redirect(checkout_session.url, code=303)
