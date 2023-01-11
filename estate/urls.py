from django.urls import path, include
from .views import *

app_name="estate"

urlpatterns = [

    ####################################################################################################

                                    ## ACTION SUR LES PROPRIETES ##

    ####################################################################################################
    
    path('list-des-proprietees/', ListEstate, name="list-des-propriete"),
    path('creer-une-proprietie/', CreatePropreite, name="creer-propriete"),
    path('update-proprietie/', UpdatePropriete, name="modifier-propriete"),
    path('remove-proprietie/', DeletePropreite, name="supprime-propriete"),
    path('details-de-proprietees/', DetailsPropreite, name="details-propriete"),

    ####################################################################################################

                            ## ACTION SUR LES OPTIONS DES PROPRIETES ##

    ####################################################################################################   

    path('create-proprietee-options/',CreatePropOptions, name="create-proprietee-options"),
    path('update-proprietee-options/<int:pk>/',UpdatePropOptions, name="update-proprietee-options"),
    path('details-proprietee-options/<int:pk>/',detailsPropOptions, name="details-proprietee-options"),
    path('delete-proprietee-options/<int:pk>/',DeletePropOptions, name="delete-proprietee-options"),
    path('liste-proprietee-options/',ListPropOptions, name="liste-proprietee-options"),

    ####################################################################################################

                                    ## ACTION SUR LES TYPES ##

    ####################################################################################################
     
    path('create-proprietee-type/',CreateType, name="create-proprietee-type"),
    path('update-proprietee-type/<int:pk>/',UpdateType, name="update-proprietee-type"),
    path('details-proprietee-type/<int:pk>/',DetailsType, name="details-proprietee-type"),
    path('delete-proprietee-type/<int:pk>/',DeleteType, name="delete-proprietee-type"),
    path('liste-proprietee-type/',ListeType, name="liste-proprietee-type"),

]


