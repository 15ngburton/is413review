from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from manager import models as mmod
from django.http import HttpResponseRedirect

@view_function
def process_request(request, prod: mmod.Product):

    if prod is None:
        return HttpResponseRedirect('/catalog/index/')
    else:

        pictures = prod.image_urls()
        mainpic = prod.image_url()

        if prod in request.last_five:
            request.last_five.remove(prod)
        request.last_five.insert(0, prod)
        request.last_five = request.last_five[:6]

        print(">>>>>>>>>>>", pictures[0])

    context = {
        'pictures': pictures,
        'mainpic': mainpic,
        'itemname': prod.name,
        'ptype': prod.TITLE,
        'qty':prod.get_quantity(),

    }
    return request.dmp.render('details.html', context)
