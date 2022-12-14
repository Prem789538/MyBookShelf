from django.db import models

# Create your models here.

class User(models.Model):
    full_name = models.CharField(max_length=100,null=False)
    email = models.EmailField(null=False,unique=True)
    password = models.CharField(max_length=100,null=False)

