from django.shortcuts import render,redirect
from StoreBranch.forms import BranchForm
from StoreBranch.models import Branch,Product

# Create your views here.

def branch(request):
    if request.method == "POST":
        form = BranchForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = BranchForm()
    return render(request,'hub.html',{'form':form})

def show(request):
    branches = Branch.objects.all()
    return render(request,'show.html',{'branches':branches})

def edit(request,id):
    branch = Branch.objects.get(id=id)
    return render(request,'edit.html',{'branch':branch})

def update(request,id):
    branch = Branch.objects.get(id=id)
    form = BranchForm(request.POST,instance=branch)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,'edit.html',{'branch':branch})

def destroy(request,id):
    branch = Branch.objects.get(id=id)
    branch.delete()
    return redirect("/show") 

