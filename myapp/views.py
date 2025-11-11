from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return render(request, "index.html")

def hello(request, username):
    print(f"Username received: {username}")
    return HttpResponse("<h2>Hello %s</h2>" % username)

def about(request):
    return render(request, "about.html")

def projects(request):
    #projects = list(Project.objects.values())
    return render(request, "projects.html")

def tasks(request):
    #task = Task.objects.get(id=id)
    #task = get_object_or_404(Task, id=id)
    return render(request, "tasks.html")