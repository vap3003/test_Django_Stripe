from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
import stripe
from .models import Item
from django.views import View


def item(request, id):
    item = get_object_or_404(Item, id=id)
    template = 'item.html'
    api_key = settings.STRIPE_PUBLISHABLE_KEY
    context = {
        'item': item,
        'api_key': api_key
    }
    return render(request, template, context)        


def buy(request, id):
    if request.method == 'GET':
        item = get_object_or_404(Item, id=id)
        domain = "https://tap-django-stripe.herokuapp.com"
        if settings.DEBUG:
            domain = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': item.price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url = domain + '/success/',
            cancel_url = domain + '/cancel/',
        )
        return checkout_session


        #     return JsonResponse({'sessionId': checkout_session['id']})
        # except Exception as e:
        #     return JsonResponse({'error': str(e)})