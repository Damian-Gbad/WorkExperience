from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>My first django website</h1>")

def version1(response):
    return HttpResponse("<h1>View one</h1>")