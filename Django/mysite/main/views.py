from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreatNewList

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True

                else:
                    item.complete = False

                item.save()


        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)

            else:
                print("invalid")


    return render(response, "main/list.html", {"ls": ls})

def home(response):
    return render(response, "main/home.html", {})

def view(response):
   all_lists = ToDoList.objects.all()
   count = 1
   return render(response, "main/view_list.html", {"all_lists":all_lists, "count":count})

def register(response):
    return render(response, "main/register/register.html", {})

def create(response):
    jeff = response.user.todolist.all
    if response.method == "POST":
        form = CreatNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)

            return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreatNewList()
    return render(response, "main/create.html", {"form":form, "jeff":jeff})

