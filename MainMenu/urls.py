from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.Mindex),
<<<<<<< HEAD
    path('branches/', include('StoreBranch.urls')),
    path('clients/', include('Clients.urls')),
    path('logout/',   views.Logout)
=======
    path('branches/',include('StoreBranch.urls')),
    path('clients/',include('Clients.urls'))
>>>>>>> refs/remotes/origin/main
]