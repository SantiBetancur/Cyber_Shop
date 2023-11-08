from django.contrib import admin
from django.urls import path
from StoreBranch import views

urlpatterns = [
    path('insert/',views.insertBranch),
    path('branches/',views.showBranches),
    path('show/<int:branchId>',views.showDetails),
    path('update/<int:branchId>',views.update),
    path('delete/<int:branchId>',views.delete)

]