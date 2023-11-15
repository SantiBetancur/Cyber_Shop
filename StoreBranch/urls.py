from django.contrib import admin
from django.urls import path
from StoreBranch import views

urlpatterns = [
    path('insert/',views.insertBranch),
    path('',views.showBranches),
    path('show/<int:branchId>',views.showDetails),
    path('update/<int:branchId>',views.update),
    path('delete/<int:branchId>',views.delete),
    path('show/showProducts/addProduct/',views.insertProduct),
    path('show/showProducts/<int:branchId>',views.showProducts),
    path('show/showProducts/showProductDetails/<int:productId>',views.showProductDetail),
    path('show/showProducts/updateProduct/<int:branchId>/<int:productId>',views.updateProduct),
    path('show/showProducts/deleteProduct/<int:branchId>/<int:productId>',views.deleteProduct),
    path('show/showProducts/history/', views.stockHistory),
    path('history/', views.branchesHistory)
]