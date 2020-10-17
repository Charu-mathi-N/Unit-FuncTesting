from django.db import models


# Create your models here.

class Hash(models.Model):
    text = models.TextField()
    hashed = models.CharField(max_length = 64)
