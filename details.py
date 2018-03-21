from django_mako_plus import view_function
from django import forms
from django.http import HttpResponseRedirect
from formlib import Formless
from catalog import models as cmod
from django.contrib import auth
import math

@view_function
def process_request(request, prodID:int=0):
    if prodID == 0:
        return HttpResponseRedirect("/catalog/index/")
    else:
        product = cmod.Product.objects.get(id = prodID)
        category = product.category_id.name
    context = {
        'product': product,
        'category': category,
    }
    return request.dmp.render('productpage.html', context)
