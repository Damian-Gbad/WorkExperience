from django.urls import path
from . import views

urlpatterns = [
path("<int:id>", views.index, name= "index"), 
path("", views.home, name ="home"),
path("home/", views.home, name ="home"),
# path("view_list/", views.view, name="view_list"),
path("create/", views.create, name="create"), 
 # path("view_list/<int:id>/",  views.index, name= "index"),
]