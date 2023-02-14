from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='home'),
    path('item/<int:id>', views.item, name='item'),
    path('buy/<id>/', views.buy, name='buy'),
]
