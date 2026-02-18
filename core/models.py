from django.db import models

class RegisterUser(models.Model):
    name = models.CharField(max_length=100)