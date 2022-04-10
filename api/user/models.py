from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=255, verbose_name="Name")
    email =models.EmailField(verbose_name="Email")
    password=models.CharField(max_length=255, verbose_name="Password")
    status_delete=models.BooleanField(default=False, verbose_name= "Status")

class Meta: 
    db_table = "Users"
