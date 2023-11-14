from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User



# Create your views here.

def Mindex(request):
    
    return render(request,'mindex.html',{'get_username':request.POST['username']})
