from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 25)
    first_name = models.CharField(max_length = 20, default = username)
    last_name = models.CharField(max_length = 20, default = "")
    password = models.CharField()
    email = models.EmailField()

