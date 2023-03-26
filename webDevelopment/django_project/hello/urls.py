from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name = "index"),
    path("aadhar/", views.aadhar, name = "aadhar"), 
    path("<str:name>", views.greet, name= "greet")
]
