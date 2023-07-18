from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(upload_to ='static/images', default='defaultimage.jpg',null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    objects = models.Manager()
    def __str__(self):
        return self.name



class Alimlar(models.Model):
    adet = models.IntegerField(max_length=20, null=False)
    tarih = models.DateTimeField(auto_now_add=True, null=True)
    fiyat = models.CharField(max_length=50)
    objects = models.Manager()



class Satimlar(models.Model):
    adet = models.CharField(max_length=20, null=False)
    tarih = models.DateTimeField(auto_now_add=True, null=True)
    fiyat = models.CharField(max_length=50)
    objects = models.Manager()
