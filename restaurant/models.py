from django.db import models

# Create your models here.


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length = 256)
    strasse = models.CharField(max_length = 256)
    stadt = models.CharField(max_length = 256)
    kueche = models.CharField(max_length = 256)
    tel_nr = models.CharField(max_length = 256)
    homepage = models.CharField(max_length = 256)
    oeffnungszeiten = models.CharField(max_length = 256)

class Wunschliste(models.Model):
    wunsch_gericht = models.CharField(max_length = 256)
    restaurant_name = models.ForeignKey(Restaurant,related_name = 'wunschliste', on_delete=models.CASCADE)
    preis = models.PositiveIntegerField()

class Menu(models.Model):
    restaurant_name = models.ForeignKey(Restaurant,related_name = 'menu', on_delete=models.CASCADE)
    gericht_name = models.CharField(max_length = 256)
    kueche = models.CharField(max_length = 256)
    preis = models.PositiveIntegerField()
