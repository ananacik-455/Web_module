from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

# Create your views here.

def my_view(request):
    return  HttpResponse("Init view")

def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.path


    return HttpResponse(f"""
        <p>Host: {host}</p>
        <p>User agent: {user_agent}</p>
        <p>Path: {path}</p>
    """, headers={"SecretCode": "12341232345"})

def about(request, name, age):
    return HttpResponse(f"""
        <h2>About user</h2>
        <p>Name: {name}</p>
        <p>Age: {age}</p>
""")

def contact(request):
    get_params = request.GET
#     print(get_params)
#     print(type(get_params))
#     response = f"""
#         <h2>Contacts</h2>
#         <br>
# """

    return HttpResponse(f"Hello {get_params.get('name', 'No Name')}, your {get_params.get('prog_lan', 'Python')} knowledge is awesome!")

# Hello {name}, your {prog_lan} knowledge is awesome!

def example_view(request, *args, **kwargs):
    arg1 = args[0] if args else None
    kwarg1 = kwargs.get("param1")

    return HttpResponse(f"Positional args: {arg1}, Name kwargs: {kwarg1}")

def article_year(request, year):
    return HttpResponse(f"Article from {year} year!")



class MyView(View):

    def get(self, request):
        return HttpResponse("Class view example.")


def register(request, name="Unknown", age=0):

    return HttpResponse(f"""
        <h2>Name: {name}</h2>
        <h2>Age: {age}</h2>
    """)



