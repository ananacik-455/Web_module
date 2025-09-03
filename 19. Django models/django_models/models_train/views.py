from django.shortcuts import render, redirect
# from .models import Person
from .models import Person
# Create your views here.


def index(request):
    people = Person.objects.all()
    return render(request, 'models_train/index.html', {"people": people})


def create(request):
    if request.method == "POST":
        data = request.POST
        Person.objects.create(
            name=data.get("name"),
            age=data.get("age"),
        )
    return redirect("index")

def edit(request, id):
    try:
        person = Person.objects.get(id=id)
        if request.method == "POST":
            data = request.POST
            person.name = data.get("name")
            person.age = data.get("age")
            person.save()
            return redirect("index")
        else:
            return render(request, "models_train/edit.html", {"person": person})
    except Person.DoesNotExist:
        return redirect("index")

def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return redirect("index")
    except Person.DoesNotExist:
        return redirect("index")




# def test_query():
#     print("Start Test query", flush=True)
#     people = Person.objects.all()
#     print(people.query, flush=True)
#
#     people = people.filter(name="Tom")
#     print(people.query, flush=True)
#
#     people = people.filter(age=31)
#     print(people.query, flush=True)
#
#
#
#
#
#
# test_query()
