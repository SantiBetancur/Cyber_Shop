from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import logout, get_user





# Create your views here.

def Mindex(request):
    u = get_user(request)
    c_user = ""
    if u.is_authenticated:
        c_user = u

    return render(request,'mindex.html', {'get_username':c_user})


def Logout(request):
    logout(request)
    return redirect('/')#login

