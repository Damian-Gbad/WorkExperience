from django.urls import path
from . import views

urlpatterns = [
path("", views.index, name= "index"), 
path("version1/", views.version1, name= "view 1"), 
]