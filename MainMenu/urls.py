from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.Mindex),
    path('branches/', include('StoreBranch.urls')),
    path('clients/', include('Clients.urls')),
    path('logout/',   views.Logout)
    ]