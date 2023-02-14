from http.client import HTTPResponse
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
import stripe
from .models import Item
from django.views import View
from django.urls import reverse


def item(request, id):
    item = get_object_or_404(Item, id=id)
    template = 'item.html'
    api_key = settings.STRIPE_PUBLISHABLE_KEY
    context = {
        'item': item,
        'api_key': api_key
    }
    return render(request, template, context)        


# def buy(request, id):
#     if request.method == 'GET':
#         item = get_object_or_404(Item, id=id)
#         domain = 'https://tap-django-stripe.herokuapp.com'
#         stripe.api_key = settings.STRIPE_PUBLISHABLE_KEY
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[
#                 {
#                     'name': item.name,
#                     'quantity': 1,
#                     'currency': 'usd',
#                     'amount': item.price
#                 },
#             ],
#             mode='payment',
#             success_url = domain + '/success/',
#             cancel_url = domain + '/cancel/',
#         )
#         return stripe.redirectToCheckout( 'sessionId': checkout_session.id)
        # return JsonResponse({'sessionId': checkout_session['id']})


        #     return JsonResponse({'sessionId': checkout_session['id']})
        # except Exception as e:
        #     return JsonResponse({'error': str(e)})

@csrf_exempt
def create_checkout_session(request, id):
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
    # return JsonResponse({'sessionId': checkout_session.id})