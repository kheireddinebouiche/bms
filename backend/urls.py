from django.urls import path, include
from .views import *
from app.views import *

app_name="backend"

urlpatterns = [

   path('',BackIndex,name="index"),
   path('configuration-societe/',ConfigurationSociete, name="conf-societe"),

   path('mon-compte/',EntrepriseProfile, name="mon-compte"),
   
   path('tables/',Tables, name="tables"),

   path('ajouter-un-service/',CreatService, name="ajouter-service"),
   path('liste-des-services/',ListService, name="liste-des-services"),
   path('mes-services/',ShowServicesBySociete,name="show-my-services"),
   path('mise-a-jours-service/<int:pk>/',UpdateService,name="mise-a-jour-service"),

   path('creer-un-ticket/',CreateTicket,name="creer-un-ticket"),
   path('mise-a-jours-ticket/',UpdateTicket,name="mise-a-jours-ticket"),
   path('liste-des-tickets/',ListeTicket,name="liste-des-tickets"),
   path('supprimer-un-ticket/<int:pk>/',RemoveTicket,name="supprimer-un-ticket"),
   path('rechercher-un-ticket/',SearchTicket,name="rechercher-un-ticket"),
   path('liste-de-mes-tickes/',ListDeMesTicket, name="liste-de-mes-tickets"),
   
   path('creer-type-ticket/',CreateTicketType,name="creer-type-ticket"),
   path('mise-a-jours-type-ticket/',UpdateTicketType,name="mise-a-jours-type-ticket"),
   path('liste-type-ticket/',ListeTicketType,name="liste-type-ticket"),
   path('supprimer-type-ticket/',RemoveTicketType,name="supprimer-type-ticket"),
   path('rechercher-type-ticket/',SearchTicketType,name="rechercher-type-ticket"),

   path('ajouter-un-secteur/',CreateSecteur, name="ajouter-un-secteur"),
   path('liste-des-secteurs/',ListeSecteur,name="liste-des-secteurs"),
   path('supprimer-un-secteur/',RemoveSecteur, name="supprimer-un-secteur"),

   path('create-categorie/',CreateCategorie, name="create-categorie"),
   path('liste-categorie/',ListeCategorie, name="list-categorie"),
   path('mise-a-jour-categorie/<int:pk>/',UpdateCategorie, name="update-categorie"),
   path('suppression-categorie/<int:pk>/', DeleteSecteur, name="delete-categorie"),

   path('configuration-societe/', ConfigreMySociete, name="configuration-societe"),
   
   path('list-des-messages/',ListContact, name="list-contact"),
   path('details-message/<int:pk>/',DetailsContact, name='details-contact'),
   path('supprimer-contact/<int:pk>/',RemoveContact, name='supprimer-contact'),

   path('liste-pros/', ListPros, name="liste-profs"),
   path('liste-clients/', ListClient, name="liste-client"),
   path('details-du-compte/<int:pk>/',DetailsProfile,name="details-compte" ),
   path('suspension-de-compte/<int:pk>/',SuspendProfile, name="suspension-compte"),
   path('supprimer-compte/<int:pk>/',RemovePofile, name="supprimer-compte"),
   path('activation-compte/<int:pk>/',ActivateProfile, name="activation-compte"),
   path('desactivation-compte/<int:pk>/', DeactivateProfile, name="desactivation-compte"),
   path('list-demande-inscription-ag/',ListDemandeAgImm, name="demande-inscription-ag"),


]


