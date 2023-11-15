from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from StoreBranch.forms import BranchForm,ProductForm
from .models import Branch, Stock, productHistory, branchHistory
from django.db import connection

# Create your views here.

def insertBranch(request):
    context = {}
    form = BranchForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/main/branches")
    context["form"] = form
    return render(request,"createView.html",context)

def insertProduct(request):
    context = {}
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/main/branches/")
    context["form"] = form
    return render(request, "createProduct.html", context)


def showBranches(request):
    context = {}
    context["dataset"] = Branch.objects.all() 

    #call a msql function
    cursor = connection.cursor()
    query = "SELECT ammount_of_branches()"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    context['b_result'] = result
    cursor.close() 

    return render(request,"showBranches.html",context)

def showProducts(request,branchId):
    context = {}
    context["dataset"] = Stock.objects.filter(productBranchId=branchId)

    cursor = connection.cursor()
    query = "SELECT ammount_of_products(%s)"
    attr = (branchId,)
    cursor.execute(query, attr)
    result = cursor.fetchone()[0]
    context['p_result'] = result
    return render(request,"showProducts.html",context)

def showDetails(request,branchId):
    context = {}
    context["data"] = Branch.objects.get(branchId=branchId)
    return render(request,"showDetails.html",context)

def showProductDetail(request,productId):
    context = {}
    context["data"] = Stock.objects.get(productId=productId)
    return render(request,"showProductDetail.html",context)

def update(request,branchId):
    context = {}
    obj = get_object_or_404(Branch,branchId=branchId)
    form = BranchForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/main/branches")
    
    context["form"] = form

    return render(request,"update.html",context)

def updateProduct(request,branchId,productId):
    context = {}
    obj = get_object_or_404(Stock,productId=productId)
    form = ProductForm(request.POST or None,instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/main/branches/show/"+str(branchId))
    context["form"] = form
    return render(request,"updateProduct.html",context)

def delete(request,branchId):
    context = {}
    obj = get_object_or_404(Branch,branchId=branchId)
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect("/main/branches")
    return render(request,"delete.html",context)

def deleteProduct(request,branchId,productId):
    context = {}
    obj = get_object_or_404(Stock,productId=productId)
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect("/main/branches/show/showProducts/"+str(branchId))
    return render(request,"deleteProduct.html",context)

def stockHistory(request):
    context = {}
    context["dataset"] = productHistory.objects.all()
    return render(request, 'productHistory.html', context)

def branchesHistory(request):
    context = {}
    context["dataset"] = branchHistory.objects.all()
    return render(request, 'branchHistory.html', context)
