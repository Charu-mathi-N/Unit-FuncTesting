from django.db import models


# Create your models here.

class hash(models.Model):
    text = models.TextField()
    text_hash= models.CharField(max_length = 64)
