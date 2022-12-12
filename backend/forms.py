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
        fields = ('designation','adresse','telephone','email','secteur','categorie')


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

