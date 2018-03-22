from catalog import models as cmod

class LastFiveMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        last_five_list = request.session.get('last_five_ids', []) #Get the last-viewed product id list from the session

        product_list = [] #this is a list of the objects converted from the ids.

        for id in last_five_list: #Convert the product ids from integers to actual products
            product_list.insert(0, cmod.Product.objects.filter(id = id).first())

        request.last_five = product_list #Attach to the request object.

        response = self.get_response(request)

        if len(last_five_list) > 6:
            request.last_five.pop()

        id_list = []

        for object in request.last_five[:6]:
            id_list.insert(0, object.id)

        request.session["last_five_ids"] = id_list

        return response
