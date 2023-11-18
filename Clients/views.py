from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from .models import ClientInfo,clientPhones,Person,Corporation,historyPerson,historyCorp
from .forms import ClientForm,CorporationForm,PersonForm
from django.db import connection

# Create your views here.

def newPerson(request):
    context = {}
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/main/clients")
    context["form"] = form
    return render(request,"newPerson.html",context)

def showPersons(request):
    context = {}
    context["dataset"] = Person.objects.all()
    return render(request,"showPersons.html",context)

def showClients(request):
    return render(request,"clientsMenu.html")

def newCorporation(request):
    context = {}
    form = CorporationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/main/clients")
    context["form"] = form
    return render(request,"newCorp.html",context)

def showCorps(request):
    context = {}
    context["dataset"] = Corporation.objects.all()
    return render(request,"showCorps.html",context)

'''def deletePerson(request,id):
    context = {}
    person = get_object_or_404(Person, clientinfo_ptr_id = id)
    client = get_object_or_404(ClientInfo,id = id)

    if request.method == 'POST':
        person.delete()
        
        return HttpResponseRedirect("/main/clients/showPersons")
    return render(request,"deletePerson.html",context)

def deleteCorp(request,id):
    context = {}
    obj = get_object_or_404(Corporation,id=id)
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect("/main/clients/showCorps")
    return render(request,"deleteCorp.html",context)
'''
def personHistory(request):
    context = {}
    context["dataset"] = historyPerson.objects.all()
    return render(request, 'personHistory.html', context)

def corpHistory(request):
    context = {}
    context["dataset"] = historyCorp.objects.all()
    return render(request, 'corpHistory.html', context)  

def clientType(request):
    context = {}
    return render(request,'clientType.html',context) 

def clientType1(request,id):
    context = {}
    cursor = connection.cursor()
    result = cursor.callproc("tipoCliente",[id])
    result = cursor.fetchone()[0]
    if result == 2:
        res = "Corporation"
    elif result == 1:
        res = "Person"
    else:
        res = "Error"
    context['b_result'] = res
    cursor.close()     
    return render(request,"clientType1.html",context)

