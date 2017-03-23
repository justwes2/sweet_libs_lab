from django.shortcuts import HttpResponse
# make sure to change the above to HttpResponse, it is not the default, and not doing so will prevent the view from rendering

def index(request):
    return HttpResponse("Hello, world. You're at the polls index")
# this simple view will render the text above at the defined path. 
