from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from .views import *


app_name="app"

urlpatterns = [
    path('', index, name='index'),
    path('login/',LoginView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(), name="logout"), 
    path('mon-profile/', MyProfile, name='mon-profile'),

    path('inscription/', RegisterClient, name="register_client"),
    path('devenir-membre/', RegisterPro, name="register-pro"),
    path('devenir-membre/vendeur/', RegisterSellerParticulier, name="register-seller-ind"),
    path('devenir-membre/agence/', RegisterSellerEntreprise, name="register-seller-ent"),

    path('liste-professionnels/',ListPro, name="liste-pros"),
    path('choisir-mon-plan/',PlaneChoice, name="inscription-etape-1"),
    path('tableau-de-bord/',EnterBackEnd, name="administration"),
    path('notification/',RedirectRegister, name="notification-register"),
    path('mise-a-jours-profile/', UpdateProfile, name="mise-a-jour-profile"),
    path('conditions-general-d-utilisation/',CGU, name="cgu"),
    path('terms/',Terms, name="terms"),
    path('societes/',ListeSociete, name="list-societe"),

    path('recherche-societe/', SocieteSearchList.as_view(), name="rech-societe"),
    
    path('categorie/', getCategorie, name="categorie")

    
    
]
