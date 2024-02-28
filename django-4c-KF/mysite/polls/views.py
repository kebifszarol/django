from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def counter(request):
    template = loader.get_template('counter.html')
    context = {}
    return HttpResponse(template.render(context, request))