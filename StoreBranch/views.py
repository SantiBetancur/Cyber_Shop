from django.shortcuts import render,redirect,get_object_or_404
from StoreBranch.forms import BranchForm
from .models import Branch,Product

# Create your views here.

def insertBranch(request):
    context = {}
    form = BranchForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request,"createView.html",context)

def showBranches(request):
    context = {}
    context["dataset"] = Branch.objects.all()   
    return render(request,"showBranches.html",context)

def showDetails(request,id):
    context = {}
    context["data"] = Branch.objects.get(branchId=id)
    return render(request,"showDetails.html",context)