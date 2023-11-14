from django.shortcuts import render,get_list_or_404,HttpResponseRedirect
from .models import ClientInfo,clientPhones,Person,Corporation
from .forms import ClientForm,CorporationForm,PersonForm,PhonesForm

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

#def newPhone(request,idCorp)