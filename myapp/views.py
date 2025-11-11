from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return HttpResponse("<h1>Index Page</h1>")

def hello(request, username):
    print(f"Username received: {username}")
    return HttpResponse("<h2>Hello %s</h2>" % username)

def about(request):
    return HttpResponse("<h2>About Page</h2>")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    #task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return JsonResponse("Task: %s" % task.title, safe=False)