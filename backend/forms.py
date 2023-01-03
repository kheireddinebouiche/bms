from django import forms
from django.forms.fields import ChoiceField
from .models import *
from app.models import *
from .forms import *
from django.forms import ModelForm, TextInput, EmailInput, widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField


class CreateServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ('designation',)
        widgets = {
            'designation' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Veuillez entrer un nom à votre service...',
                'label' : 'Déscription :'
            })
        }

class UpdateServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ('designation','entreprise')

class ConfigurationSocieteForm(forms.ModelForm):
    class Meta:
        model = Societe
        labels = {
            'designation':"Raison social / Dénomination votre entreprise : *",
            'pays' : "Votre pays de domiciliation : *",
            'province' : "Province : *",
            'adresse': "Adresse : ",
            'adresse_2': "Adresse 2 : ",
            'rue' : 'N° Rue :',
            'num_dep': "Département : ",
            
        }
        fields = ('designation','pays','province','adresse','adresse_2','num_dep','rue','telephone','email','secteur','categorie')
        widgets = {
            'designation' : TextInput(attrs={
                'class' : 'form-control mb-3',
            }),
            'pays' : forms.Select(attrs={
                'class' : 'form-control mb-3',
            }),
            'province' : TextInput(attrs={
                'class' : 'form-control mb-3',
                'placeholder': "Etat/Ville..."
            }),
            'adresse' : TextInput(attrs={
                'class' : 'form-control mb-3',
                
                
            }),
            'adresse_2' : TextInput(attrs={
                'class' : 'form-control mb-3',
                
            }),
            'rue' : TextInput(attrs={
                'class' : 'form-control mb-3',
                
            }),
            'num_dep' : TextInput(attrs={
                'class' : 'form-control mb-3',
            }),
        }


class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('message','type')

class CreateTypeTicketForm(forms.ModelForm):
    class Meta:
        model = TypeTicket
        fields = ('designation',)
        widgets = {
            'designation' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Veuillez renseigner une description de la catégorie...',
            
            })
        }

