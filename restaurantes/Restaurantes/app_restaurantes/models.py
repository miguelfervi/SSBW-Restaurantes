from django.db import models
from mongoengine import *

class Restaurante (models.Model):
    nombre    = models.CharField(max_length=30, unique=True)
    direccion = models.CharField(max_length=60)
    email= models.CharField(max_length=60)
    imagen = models.CharField(max_length = 150, blank = True)
    me_gusta  = models.IntegerField(blank=True)
    id = models.IntegerField(primary_key=True)
    

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.nombre


connect('platos')
 #Con mongoengine
class Platos(Document):
	nombre    = StringField(max_length=30, unique=True)
	imagen    = StringField(max_length = 150, blank = True)
	precio    = FloatField(blank = True)
	nombre_res    = StringField(blank = True)