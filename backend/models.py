from django.db import models
from app.models import *
from django.contrib.auth.models import User

class Services(models.Model):
    designation = models.CharField(max_length=300 ,null=True, blank=True)
    entreprise = models.ForeignKey(Societe, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Services"
        verbose_name = "Service"

    def __str__(self):
        return self.designation

class CatService(models.Model):
    pass

class SendMessage(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    object = models.CharField(max_length=300, null=True, blank=True)
    message = models.TextField(max_length=3000, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name="Message"
        verbose_name_plural="Messages"

    def __str__(self):
        return self.user

class TypeTicket(models.Model):
    designation = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name="Type de ticket"
        verbose_name_plural="Types des tickets"
    
    def __str__(self):
        return self.designation

class Ticket(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    message = models.TextField(max_length=4000, null=True, blank=True)
    type = models.ForeignKey(TypeTicket, null=True, blank=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

class Notifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Notification"
        verbose_name="Notifications"

    def __str__(self):
        return self.description