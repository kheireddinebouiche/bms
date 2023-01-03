from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TypePropriete(models.Model):
    designation = models.CharField(max_length=1000, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True, blank=True)

    class Meta:
        verbose_name = "Type de propriété"
        verbose_name_plural = "Types des proprirétés"

    def __str__(self):
        return self.designation


RENTAL_CHOICE= {
    ('jou', 'Par jour'),
    ('moi', 'Par mois'),
    ('ann', 'Par année'),

}    

class Proprietes(models.Model):
    user = models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE)

    designation  = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=4000, null=True, blank=True)

    superficie = models.DecimalField(max_digits=10,null=True, blank=True, decimal_places=2)

    adresse = models.CharField(max_length=100, null=True, blank=True)
    adresse_2 = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.CharField(max_length=200,null=True, blank=True)
    province = models.CharField(max_length=200,null=True, blank=True)
    etat= models.CharField(max_length=200,null=True, blank=True)

    selling_price = models.DecimalField(max_digits=10,null=True, blank=True, decimal_places=2)
    rental_price = models.DecimalField(max_digits=10,null=True, blank=True, decimal_places=2)
    rental_mode = models.CharField(max_length=3, choices=RENTAL_CHOICE ,null=True, blank=True) 

    type = models.ForeignKey(TypePropriete,null=True, blank=True, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    class Meta:
        verbose_name="Proprietée"
        verbose_name_plural = "Proporietées"
    def __str__(self):
        return self.designation


class SellingAndRentalProprieties(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    propriete = models.ForeignKey(Proprietes, null=True, blank=True, on_delete=models.CASCADE)

    is_selling  = models.BooleanField(null=True, blank=True)
    is_rental   = models.BooleanField(null=True, blank=True)

    created_at  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.propriete


class ImagesPropreite(models.Model):
    propriete = models.ForeignKey(Proprietes, null=True, blank=True, on_delete=models.CASCADE)

    image = models.ImageField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name="Image d'une propriétée"
        verbose_name="Images des propriétées"
        
    def __str__(self):
        return self.propriete

class ProprieteOptions(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    description = models.CharField(max_length=100, null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    

    class Meta:
        verbose_name="Options de la propriétée"
        verbose_name_plural="Options des propriétées"

    def __str__(self):
        return self.description