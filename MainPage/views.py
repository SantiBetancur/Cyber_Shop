from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import login_users
from django.shortcuts import render
from .forms import Login_form

# Create your views here.
#def hello(request):
#   return HttpResponse("<h1>Hello World</h1>")

def index(request):
    
    return render(request, 'index.html', {'form': Login_form})

'''def hello(request, username):
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

    return HttpResponse("<h1>Task: %s</h1>" % task)'''
