
from catalog import models as cmod

class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        # Call the last five from the session
        request.last_five = []
        pids = request.session.get('history', [])  # bring in the past history from the session
        request.last_five = []  # initialize the objects list

        for pid in pids:
            request.last_five.append(cmod.Product.objects.get(id=pid))  # populate the objects list from the past session history


        response = self.get_response(request)

        pathlist = request.path.split('/')
        if len(pathlist) > 3:
            if pathlist[2] == 'detail':
                if pathlist[len(pathlist)-1] is not '':
                    id = pathlist[len(pathlist)-1]  # Grab the id from the current page
                    request.last_five.insert(0, cmod.Product.objects.get(id=id))  # add the current id to the objects list
                    print(request.last_five.count(cmod.Product.objects.get(id=pathlist[len(pathlist)-1])))
                    if request.last_five.count(cmod.Product.objects.get(id=pathlist[len(pathlist)-1])) > 1:
                        request.last_five.reverse()
                        request.last_five.remove(cmod.Product.objects.get(id=pathlist[len(pathlist)-1]))
                        request.last_five.reverse()
                    fiveobjects = []
                    for p in request.last_five[:5]:
                        print(p)
                        fiveobjects.append(p)
                    request.last_five = fiveobjects

        pids = []
        for p in request.last_five:
            pids.append(p.id)

        if len(pathlist) > 3:
            if pathlist[2] == 'detail':
                if pathlist[len(pathlist)-1] is not '':
                    request.session['history'] = pids


        return response






        # while len(request.last_five) > 5:
        #     request.last_five.pop()
        #
        # if request.last_five.count(cmod.Product.objects.get(id=request.dmp.urlparams[0])) == 2:
        #     request.last_five.remove(cmod.Product.objects.get(id=request.dmp.urlparams[0]))
