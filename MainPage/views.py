from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .forms import Login_form, Register_form

# Create your views here.
#def hello(request):
#   return HttpResponse("<h1>Hello World</h1>")

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {'form': Login_form()})
    else:
     
        #Request info from the database    
        try:
            get_user = User.objects.get(username = request.POST['username']).username

            if (check_password(request.POST['password'], 
                            User.objects.get(username = get_user).password)): 
            
                return redirect('/main/')
        
            return render(request, 'index.html', 
                        {'form': Login_form(), 'login_error':'Incorrect Username or Password'})
        except:
        
            return render(request, 'index.html', 
                        {'form': Login_form(), 'login_error':'Incorrect Username or Password'})
        


def register(request):
                   
     
          
    if request.method == 'GET':
        return render(request, 'register.html',{'register':Register_form()})    
    else:
        
        try:
            validate_password(request.POST['password'])
            if request.POST['password'] == request.POST['password_confirmation']:
                #Register new user
                try:
                
                    new_user = User.objects.create_user(username = request.POST['username'], password = request.POST['password']) 
                    new_user.save()
                    return redirect("/")
                
                except:

                    return render(request, 'register.html',
                                {'register':Register_form(),'error_register':'Falied, this user already exist.'})  
                
            else:

                return render(request, 'register.html',
                            {'register':Register_form(),'error_match':'The password do not match, try again.'})  
            
        except ValidationError as e:

            print(f"La contraseña no es válida: {', '.join(e.messages)}") 
            return render(request, 'register.html',
                                {'register':Register_form(),'error_password':'Password does not meet the requeriments'})     

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
