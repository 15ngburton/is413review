from catalog import models as cmod
class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        prodIDs = []
        prodIDs = request.session.get('products')
        productList = []

        if prodIDs is not None:
            for MYid in prodIDs:
                productList.insert(0, cmod.Product.objects.get(id = MYid))

        print(request.dmp.page)

        if productList is not None:
            while len(productList) > 5:
                productList.pop()

        request.last_five = productList

        response = self.get_response(request)

        if request.dmp.page == "productpage":
            for x in request.last_five:
                if int(x.id) == int(request.dmp.urlparams[0]):
                    print("IF Check")
                    request.last_five.remove(x)

        if request.dmp.page == "productpage":
            request.last_five.insert(0, cmod.Product.objects.get(id = request.dmp.urlparams[0]))
            newProdIDs = []
            for x in request.last_five:
                newProdIDs.insert(0, x.id)

            request.session['products'] = newProdIDs

        return response
