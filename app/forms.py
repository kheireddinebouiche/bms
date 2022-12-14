from django import forms
from django.forms.fields import ChoiceField
from .models import *
from django.forms import ModelForm, TextInput, EmailInput, widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class ClientCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1')

        widgets = {
            'username' : TextInput(attrs={
                'placeholder' : "Veuillez entrer un nom d'utilisateur...",
                
            }),
            'email' : TextInput(attrs={
                'placeholder' : "Veuillez entrer une adresse email valide...",
                
            }),

            'first_name' : TextInput(attrs={
                'placeholder' : "Votre prénom...",
                
            }),
            'last_name' : TextInput(attrs={
                'placeholder' : "Votre nom...",
                
            })
        }
        
class ProCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1')
        widgets = {
            'username' : TextInput(attrs={
                'placeholder' : "Veuillez saisir un nom d'utilisateur ...",
                'class' : 'form-control',
            }),
            'email' : TextInput(attrs={
                'placeholder' : "Veuillez saisir une adresse email valide ...",
                'class' : 'form-control',
            }),
            'first_name' : TextInput(attrs={
                'placeholder' : "Votre prénom ...",
                'class' : 'form-control',
            }),
            'last_name' : TextInput(attrs={
                'placeholder' : "Votre nom ...",
                'class' : 'form-control',
            }),
            'password' : TextInput(attrs={
                'placeholder' : "Veuillez saisir un mot de passe...",
                'class' : 'form-control',
            }),
         

        }

class ProfileProForm(forms.ModelForm):
    telephone = PhoneNumberField(
            region="CA",   
            widget=PhoneNumberPrefixWidget(
                initial="FR",
                country_choices=[
                    ("CA", "Canada"),
                    ("FR", "France")
                ],                        
            ),
            label = 'Numéro de téléphone :'
           )
    class Meta:
        model = Profile
        fields = ('secteur','pays','adresse','telephone')
        labels = {
            'secteur' : "Veuillez séléctionner votre secteur d'activité :",
            'pays' : 'Pays :',
            'adresse' : "Adresse :",
        }
        widgets = {
            'pays' : forms.Select(attrs={
                'class' : 'form-control',
            }),
            'adresse' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : "N° de rue, nom de la rue"
            }),
           'secteur' : forms.Select(attrs={
            'class': 'form-control',
           })  
        }


class SellerUserForm(UserCreationForm):
    class Meta:
        model = User
        labels = {
            'Username' : "Nom d'utilisateur :",
            'email': "Votre adresse Email :",
            'first_name' : "Votre prénom :",
            'last_name' : "Votre nom :",
        }
        fields = ('username','email','first_name','last_name','password1')

        widgets = {
            'username' : TextInput(attrs={
                'placeholder' : "Veuillez entrer un nom d'utilisateur...",
                
            }),
            'email' : TextInput(attrs={
                'placeholder' : "Veuillez entrer une adresse email valide...",
                
            }),

            'first_name' : TextInput(attrs={
                'placeholder' : "Votre prénom...",
                
            }),
            'last_name' : TextInput(attrs={
                'placeholder' : "Votre nom...",
                
            })
        }

class SellerProProfileForm(forms.ModelForm):
    telephone = PhoneNumberField(
            region="CA",   
            widget=PhoneNumberPrefixWidget(
                initial="FR",
                country_choices=[
                    ("CA", "Canada"),
                    ("FR", "France")
                ],                        
            ),
            label = 'Numéro de téléphone :'
           )

        
    class Meta:
        model = Profile
        fields = ('secteur','categorie','pays','adresse','telephone')
        labels = {
            'secteur' : "Veuillez séléctionner votre secteur d'activité :",
            'categorie' : "Catégorie :",
            'pays' : 'Pays :',
            'adresse' : "Adresse :",
        }
        widgets = {
            'pays' : forms.Select(attrs={
                'class' : 'form-control',
            }),
            'adresse' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : "N° de rue, nom de la rue"
            }),
           'secteur' : forms.Select(attrs={
            'class': 'form-control',
           }), 
           'categorie' : forms.Select(attrs={
            'class' : 'form-control'
           }) 
        }
 

class SellerProfileForm(forms.ModelForm):
    telephone = PhoneNumberField(
            region="CA",   
            widget=PhoneNumberPrefixWidget(
                initial="FR",
                country_choices=[
                    ("CA", "Canada"),
                    ("FR", "France")
                ],                        
            ),
            label = 'Numéro de téléphone :'
           )
    class Meta:
        model = Profile
        fields = ('pays','adresse','telephone')
        labels = {
            'pays' : 'Pays :',
            'adresse' : "Adresse :",
        }
        widgets = {
            'pays' : forms.Select(attrs={
                'class' : 'form-control',
            }),
            'adresse' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : "N° de rue, nom de la rue"
            }),
            
        }

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
        labels = {
            'designation' : 'Nom du secteur :'
        }
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

class SocieteSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    widget=forms.TextInput(attrs={'class':'form-control','placeholder': "Secteur / Catégorie ou nom de l'entreprise que vous chercher..."})
                  )
    

    def __init__(self, *args, **kwargs):
        super(SocieteSearchForm, self).__init__(*args, **kwargs)
        self.fields['search_text'].label = ""
       

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        labels = {
            'secteur' : "Secteur d'activité :",
            'designation' : "Catégorie :"        }
        fields = ('secteur', 'designation')
        widgets = {
            'secteur' : forms.Select(attrs={
                'class' : 'form-control mb-3',

            }),
            'designation' : forms.TextInput(attrs={
                'class' : 'form-control mb-3',
            })
        }




    