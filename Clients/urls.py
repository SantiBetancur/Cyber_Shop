from django.urls import path, include
from . import views

urlpatterns = [
    path("newPerson/",views.newPerson),
    path("",views.showClients),
    path("showPersons/",views.showPersons),
    path("newCorp/",views.newCorporation),
    path("showCorps",views.showCorps)
]