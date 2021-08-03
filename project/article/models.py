from django.db import models
from django.db.models.base import Model



class textData(models.Model):
    text = models.TextField()
    label = models.TextField()
    

    def __str__(self):
        return self.label
   

# Create your models here.
