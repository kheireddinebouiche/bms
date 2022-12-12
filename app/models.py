from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class Secteur(models.Model):
    designation = models.CharField(max_length=40, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class META:
        verbose_name = "Secteur"
        verbose_name_plural = "Secteurs"
    
    def __str__(self):
        return self.designation

class Categorie(models.Model):
    designation = models.CharField(max_length=40, blank=True, null=True)
    cat = models.ForeignKey(Secteur, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class META:
        verbose_name="Catégorie"
        verbose_name_plural = "Catégories"

    def __str__(self):
        return self.designation

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=30, blank=True)
    image = models.ImageField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telephone = models.CharField(null=True, blank=True, max_length=100)   
    date_naissance = models.DateField(null=True, blank=True)
    is_client = models.BooleanField(null=True,blank=True, default=False)
    is_entreprise = models.BooleanField(null=True, blank=True)
    is_configured = models.BooleanField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Societe(models.Model):
    gerant = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length =100, null=True, blank=True)

    pays = CountryField(null=True, blank=True)
    adresse = models.CharField(max_length=30, blank=True)
    adresse_2 = models.CharField(max_length=200, null=True, blank=True)
    num_dep = models.CharField(max_length=2, null=True, blank=True)
    rue = models.CharField(max_length=40, null=True, blank=True)

    telephone = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    secteur = models.ForeignKey(Secteur, null=True, blank=True ,on_delete=models.DO_NOTHING)
    categorie = models.ForeignKey(Categorie, null=True, blank=True, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class META:
        verbose_name="Société"
        verbose_name_plural="Sociétés"

    def __str__(self):
        return self.designation

class Contact(models.Model):
    nom = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=300,null=True, blank=True)
    telephone = models.CharField(max_length=13, null=True, blank=True)
    sujet = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(max_length=4000, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name="Contact"
        verbose_name_plural="contacts"

    def __str__(self):
        return self.nom

class ReponseContact(models.Model):
    pass