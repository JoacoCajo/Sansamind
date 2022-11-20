from django.db import models

# Create your models here.
class Formul(models.Model):
    area=models.CharField(max_length=100)
    testimonio= models.CharField(max_length=1000)
    fecha= models.DateTimeField(auto_now=True)