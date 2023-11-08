from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render

# Create your views here.
#def hello(request):
#   return HttpResponse("<h1>Hello World</h1>")

def index(request):
    title = "This is the Title as a Param"
    return render(request, 'index.html', {'title': title})

def hello(request, username):
    return HttpResponse("<h1>Hello %s </h1>" % username)

def about(request):
    return HttpResponse("<h1>About</h1>")

def projects(request):

    project_list = list(Project.objects.all())
        # Create an initial HTML content
    content = "<h1>Available Projects:</h1><br>"

    # Iterate through the project_list and append each project to the content
    for project in project_list:
        content += f"<p>Project Name: {project.name}</p>"
    
    return HttpResponse(content)

def tasks(request, id):
    task = Task.objects.get(id = id).title

    return HttpResponse("<h1>Task: %s</h1>" % task)