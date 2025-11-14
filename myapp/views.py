from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from .forms import TaskForm

# Create your views here.

def index(request):
    title = "My Application Index!!"
    return render(request, "index.html", {
        "title": title})

def hello(request, username):
    print(f"Username received: {username}")
    return HttpResponse("<h2>Hello %s</h2>" % username)

def about(request):
    username = "Ovlzqz"
    return render(request, "about.html", {
        "username": username})

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.values()
    return render(request, "projects/projects.html", {
        "projects": projects})

def tasks(request):
    #task = Task.objects.get(id=id)
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html",{
        "tasks": tasks
    })

def create_task(request):
    #print(request.method)
    #print(request.GET['title'])
    #print(request.GET['description'])
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            projectkey = 2  # Default project key for simplicity
            Task.objects.create(title=title, description=description, project_id=projectkey)
            return redirect("/tasks")
    else:
        form = TaskForm()
    return render(request, "tasks/create_task.html", {
        "form": form
    })