from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm, SurveyForm

# Create your views here.

# def index(request):
#     return render(request, 'forms_train/index.html')

def index(request):
    if request.method == "POST":
        userform = UserForm(request.POST)

        if userform.is_valid():
            name = userform.cleaned_data.get("name")
            age = userform.cleaned_data.get("age")
            age = 0 if not age else age

            return HttpResponse(f"<h2>Ім'я: {name}<br>Вік: {age}</h2> ")
        else:
            return render(request, "forms_train/index_form.html", {"form": userform})

    elif request.method == "GET":
        userform = UserForm()
        return render(request, "forms_train/index_form.html", {"form": userform})

def postuser(request):
    print(request.method)



    name = request.POST.get("name", "Невідомо")
    age = request.POST.get("age", 0)

    return HttpResponse(f"<h2>Ім'я: {name}<br>Вік: {age}</h2> ")


def newform(request):
    if request.method == "POST":
        surveyform = SurveyForm(request.POST)
        if surveyform.is_valid():
            lang = surveyform.cleaned_data["favorite_language"]
            frameworks = surveyform.cleaned_data["frameworks"]
            has_experience = surveyform.cleaned_data.get("has_experience")
            start_date =  surveyform.cleaned_data["start_date"]

            response_text = f"<h2>Ваш вибір:</h2>"
            response_text += f"<p>Мова: {lang}</p>"
            response_text += f"<p>Фреймворки: {', '.join(frameworks)}</p>"
            response_text += f"<p>Досвід: {'Так' if has_experience else 'Ні'}</p>"
            response_text += f"<p>Дата: {start_date}</p>"
            return HttpResponse(response_text)
        else:
            return render(request, "forms_train/index_form.html", {"form": surveyform})

    elif request.method == "GET":
        surveyform =  SurveyForm()
        return render(request, "forms_train/index_form.html", {"form": surveyform})