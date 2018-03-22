from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
import math

@view_function
def process_request(request, product:cmod.Product):
    imagelist=product.image_urls(settings.STATIC_URL)

    if product.TITLE is 'Bulk':
        qty = product.quantity
    else:
        qty = 0;

    if product in request.last_five:
        request.last_five.remove(product)
        request.last_five.insert(0, product)
    else:
        request.last_five.insert(0, product)
        request.last_five.pop();

    context = {
        'pname': product.name,
        'img_list': product.image_urls(settings.STATIC_URL),
        'img_url': product.image_url(settings.STATIC_URL),
        'description': product.description,
        'qty': qty,
        'ptype': product.TITLE,
        'category': product.category,
        'page':1,
        jscontext('img_urls'): product.image_urls(settings.STATIC_URL),
        jscontext('img_url'): product.image_url(settings.STATIC_URL),

    }

    return request.dmp.render('details.html', context)
