from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from .views import *


app_name="app"

urlpatterns = [
    path('', index, name='index'),
    path('login/',LoginView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(), name="logout"), 
    path('mon_profile/', MyProfile, name='mon-profile'),
    path('register-client/', RegisterClient, name="register_client"),
    path('register-pro/', RegisterPro, name="register-pro"),
    path('liste-professionnels/',ListPro, name="liste-pros"),
    path('inscription-etape-1/',PlaneChoice, name="inscription-etape-1"),
    path('Tableau-de-bord/',EnterBackEnd, name="administration"),
    path('notification/',RedirectRegister, name="notification-register"),
    path('mise-a-jours-profile/', UpdateProfile, name="mise-a-jour-profile"),
    path('conditions-general-d-utilisation/',CGU, name="cgu"),
    path('terms/',Terms, name="terms"),
    
]
