from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Can ye see me noo?")
