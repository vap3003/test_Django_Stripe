import stripe
from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt

from .models import Item


def paginator(request, items_list):
    paginator = Paginator(items_list, settings.ITEMS_ON_PAGE)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


def all_items(request):
    item_list = Item.objects.all()
    page_obj = paginator(request, item_list)
    template = 'items/home.html'
    api_key = settings.STRIPE_PUBLISHABLE_KEY
    context = {
        'page_obj': page_obj,
        'api_key': api_key
    }
    return render(request, template, context)


def item(request, id):
    item = get_object_or_404(Item, id=id)
    template = 'items/item.html'
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
        success_url='https://tap-django-stripe.herokuapp.com/succses',
        cancel_url='https://tap-django-stripe.herokuapp.com/cancel',
    )
    return redirect(checkout_session.url, code=303)


def success(request):
    return HttpResponse('Success')


def cancel(request):
    return HttpResponse('Cancel')
