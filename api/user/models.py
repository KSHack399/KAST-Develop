from tokenize import Name
from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=255, verbose_name="Nombre")
    email =models.EmailField(verbose_name="Correo electrónico")
    password=models.CharField(max_length=255, verbose_name="Contraseña")
    status_delete=models.BooleanField(default=False, verbose_name= "Estado")

class Meta: 
    db_table = "Users"

class Cuentas(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, verbose_name='Nombre')
    number = models.IntegerField()
    saldo_actual = models.IntegerField()
    fecha_corte = models.DateField()
    status_delete=models.BooleanField(default=False, verbose_name= "Estado")


