from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod

@view_function
def process_request(request):
    id = request.dmp.urlparams[0]
    product = cmod.Product.objects.get(id=id)
    imgurls = []
    imgurls = product.image_urls()

    context = {
        "product": product,
        "imgurls": imgurls,
    }
    #
    return request.dmp.render('detail.html', context)
