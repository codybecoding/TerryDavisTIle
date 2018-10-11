from django.db import models

# Create your models here.


class FlooringPic(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    floor = models.ImageField(upload_to='static')

    def __str__(self):
        return self.name


class ShowerPic(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    shower = models.ImageField(upload_to='static')

    def __str__(self):
        return self.name


class KitchenPic(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    kitchen = models.ImageField(upload_to='static')

    def __str__(self):
        return self.name


class BathtubPic(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    bathtub = models.ImageField(upload_to='static')

    def __str__(self):
        return self.name


class FireplacePic(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    fireplace = models.ImageField(upload_to='static')

    def __str__(self):
        return self.name


class CountertopPic(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    countertop = models.ImageField(upload_to='static')

    def __str__(self):
        return self.name
