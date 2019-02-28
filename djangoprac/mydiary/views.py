from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>I wanted this to return a whole home page here, <br> but am not yet there</h1>")