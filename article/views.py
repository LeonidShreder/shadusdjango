from django.shortcuts import render, render_to_response
from django.http.response import  HttpResponse
from django.template.loader import get_template
from django.template import Context
# Create your views here.
def basic(request):
    view = "basic"
    html = "<html><body>this is %s view</html></body>" %view
    return HttpResponse(html)

def template_two(request):
    view = "template_two"
    return render_to_response('myview.html', {'name': view})


def template_three_simple(request):
    view = "template_three_simple"
    return render_to_response('myview.html', {'name': view})
