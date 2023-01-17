from django.shortcuts import render
from django.http import HttpResponse

# Create your views


def home(request):
    return HttpResponse("<h1>Ola mundo</h1>")
