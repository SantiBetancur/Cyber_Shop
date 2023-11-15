from django.urls import path, include
from . import views

urlpatterns = [
    path("newPerson/",views.newPerson),
    path("",views.showClients),
    path("showPersons/",views.showPersons),
    path("newCorp/",views.newCorporation),
    path("showCorps/",views.showCorps),
    
]

'''path("/deletePerson/<int:id>",views.deletePerson),
    path("deleteCorp/<int:id>",views.deleteCorp),
    path("personHistory/",views.pero),
    path("corpHistory/",views.corpHistory),'''