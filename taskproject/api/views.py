import os

import stripe
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from api.models import Item

stripe.api_key = os.getenv('STRIPE_PRIVATE_KEY')


class GetSessionId(View):
    def get(self, request, item_id, *args, **kwargs) -> JsonResponse:

        item = Item.objects.get(id=item_id)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success.html',
            cancel_url='http://localhost:8000/cancel.html',
        )

        return JsonResponse({'id': session.id})


class GetItemInfo(View):

    def get(self, request, item_id, *args, **kwargs):
        item = Item.objects.get(id=item_id)
        return render(request, "order.html", context=model_to_dict(item))
