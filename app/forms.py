from django import forms
from django.forms.fields import ChoiceField
from .models import *
from django.forms import ModelForm, TextInput, EmailInput, widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField



class ClientCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1')
        

class ProCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1')



class ProfileProForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('adresse','telephone')



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('adresse', 'telephone', 'date_naissance','image' )

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')

class SecteurCreateForm(forms.ModelForm):
    
    class Meta:
        model = Secteur
        fields = ("designation",)

        widgets  = {
            "designation" : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Veuillez entrer une désignation courte du secteur...',
            })
        }

class CreateSocieteForm(forms.ModelForm):
    class Meta:
        model = Societe
        fields = ('designation','pays','adresse','telephone','email','secteur','categorie')

class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('nom','email','telephone','sujet','message')
        widgets = {
            
            'nom' : TextInput(attrs={
                'class' : 'sm-form-control required',
            }),

            'email' : EmailInput(attrs={
                'class' : 'required email sm-form-control',
            }),

            'telephone' : TextInput(attrs={
                'class' : 'sm-form-control',
            }),

            'sujet' : TextInput(attrs={
                'class' : 'required sm-form-control',
            }),

           
            'message' : forms.Textarea(attrs={
                'class': 'required sm-form-control',
                'rows' : '6',
                'cols': '30',
            })
        }

