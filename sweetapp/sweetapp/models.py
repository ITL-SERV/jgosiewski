#models
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class TypeUser(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name = 'Nazwa')
    description = models.CharField(max_length=200, blank=True, null=True, verbose_name = 'Opis')
    is_active = models.BooleanField(default=True, verbose_name='Aktywny?')

    def __str__(self):
        return self.name
    
class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name = 'Telefon')
    type_user = models.ForeignKey(TypeUser, on_delete=models.CASCADE, blank=True, null=True, verbose_name = 'Typ użytkownika')
    

