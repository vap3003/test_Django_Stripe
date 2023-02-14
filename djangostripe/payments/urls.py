from django.urls import path
from . import views

urlpatterns = [
    # path('', views.item, name='home'),
    path('item/<int:id>', views.item, name='item'),
    # path('config/', views.stripe_config),
    # path('create-checkout-session/', views.create_checkout_session),
]
