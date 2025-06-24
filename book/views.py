from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")

def update(request):
    return HttpResponse("Update OK")

def hello_world(request):
    return HttpResponse("Hello World!")
