from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.Mindex),
    path('branches/',include('StoreBranch.urls'))
]