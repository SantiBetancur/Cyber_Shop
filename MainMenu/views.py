from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render



# Create your views here.

def Mindex(request):
    
    return render(request,'mindex.html')
