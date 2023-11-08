from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
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

def showDetails(request,branchId):
    context = {}
    context["data"] = Branch.objects.get(branchId=branchId)
    return render(request,"showDetails.html",context)

def update(request,branchId):
    context = {}
    obj = get_object_or_404(Branch,branchId=branchId)
    form = BranchForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("./"+str(branchId))
    
    context["form"] = form

    return render(request,"update.html",context)

def delete(request,branchId):
    context = {}
    obj = get_object_or_404(Branch,branchId=branchId)
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect("/hub/branches")
    return render(request,"delete.html",context)