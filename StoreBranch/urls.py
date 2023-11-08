from django.contrib import admin
from django.urls import path
from StoreBranch import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('branch',views.branch),
    path('show/',views.show),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('destroy/<int:id>',views.destroy)
]