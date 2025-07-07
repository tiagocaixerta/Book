from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return HttpResponse("Hello, world!")

@login_required
def update(request):
    return HttpResponse("Update OK")

@login_required
def hello_world(request):
    return HttpResponse("Hello World!")
