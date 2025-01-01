from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello_world(request):
    return HttpResponse("Hello world !!")


def home_page(request):
    return render(request,"index.html")
# render to load the page 
