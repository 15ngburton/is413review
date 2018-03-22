from manager import models as mmod


class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):

        #get the last five the user looked at
        #get list of ids from the session. request.session.get()
        idlist = request.session.get('fiveid', [])

        print(">>>>>>>>>>>>>>>>", idlist)
        #convert product ids into a list of product objects
        prods = []
        for id in idlist:
            prods.append(mmod.Product.objects.filter(id=id).first())

        request.last_five = prods

        if len(request.last_five) > 6:
            request.last_five.pop()

        response = self.get_response(request)

        #convert request.last_five into a list of ids
        ids = []

        for object in request.last_five[:6]:
            ids.append(object.id)


        request.session['fiveid'] = ids

        return response
