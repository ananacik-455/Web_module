from django.shortcuts import render
import datetime

# for more complex app structure
from django.template.response import TemplateResponse

# Create your views here.

def index(request):
    data = {
        "header": "Hello, Django!",
        "message": "<p>Welcome to Python world!</p>",
        "digit": -98,
        "a": 67,
        "b": -15
    }
    return render(request, "hello/index.html", context=data)

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    data = {"date": datetime.datetime.now()}
    return render(request, "hello/contact.html", context=data)


def complex_data(request):
    header = "Дані користувача"
    langs = ["Python", "Java", "C#", "Pascal"]
    user = Person("Tom", 23)
    address = ("Шевченко", 23, 45)

    data = {
        "header": header,
        "langs": langs,
        "user": user,
        "address": address,
        "range_list": list(range(1, 11)),
        "divider": 3
    }

    return render(request, "hello/complex_data.html", context=data)


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age