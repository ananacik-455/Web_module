from django.urls import path, re_path
from .views import MyView, index, article_year, example_view, register

urlpatterns = [
    path('', index, name="index"),
    path("class_view/", MyView.as_view(), name="class_view"),
    re_path(r'^articles', article_year, name="any_article", kwargs={"year": 2014}),
    path('example/<int:param1>/', example_view, name='example-detail'),
    path('register/', register, name="register"),
    path('register/<str:name>/', register, name="register"),
    path('register/<str:name>/<int:age>/', register, name="register"),
]
