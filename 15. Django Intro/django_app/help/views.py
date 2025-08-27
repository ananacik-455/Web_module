from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("HO Ho HO")

def help(request):
    return HttpResponse("GL")

def info(request):
    data = {
        "1": 1,
        "2": 2
    }

    return JsonResponse(data)
