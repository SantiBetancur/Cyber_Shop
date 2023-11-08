from django.contrib import admin
from django.urls import path
from StoreBranch import views

urlpatterns = [
    path('insert/',views.insertBranch),
    path('show/',views.showBranches),
    path('show/<int:id>',views.showDetails),

]