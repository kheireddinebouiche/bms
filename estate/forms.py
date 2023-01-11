from django import forms
from .models import *



class ProprieteForm(forms.ModelForm):
    class Meta:
        model = Proprietes
        fields = {
            'designation','description',
            'superficie','adresse',
            'adresse_2','zip_code','province','etat',
            'selling_price','rental_price','rental_mode','type'}

class TypeForm(forms.ModelForm):
    class Meta:
        model = TypePropriete
        fields = {'designation'}

class ProprieteOptionForm(forms.ModelForm):
    class Meta:
        model = ProprieteOptions
        fields = {'description','observation'}

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = {'commentaire'}
    
class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = {'reponse'}