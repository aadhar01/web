from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

#the problem with the global variable 
# is all with the url address will see the exact same list
# tasks = []
#instead we will create an session which helps to create task for each user

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value= 1, max_value=10)


# Create your views here.
def index(request):
    # this create a tasks for each session
    # check if session has the tasks if not then creates an empty list
    if "tasks" not in request.session:
        request.session["tasks"] = []
        
    return render(request, "tasks/index.html", {
        "tasks":request.session["tasks"]
        
    })
    
def add(request):
    if request.method =='POST':
        form = NewTaskForm(request.POST)
        #request.POST will have all the data that the user submitted
        
        ##this is the server side validation that need to be done
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"].append(task)
            # print(request.session["tasks"])
            # this following line after appending data takes us to the page where 
            # data has been appended
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "forms":form
            })
    # just want to get the data GET
    return render(request, "tasks/add.html", {
        "forms":NewTaskForm()
    })
    
