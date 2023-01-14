from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from datetime import datetime 
from django.contrib.auth import get_user_model
from datetime import date

class Register(models.Model):
    id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    date_birth=models.DateField(null=True)
    age=models.CharField(max_length=100,default="age")
    place=models.CharField(max_length=100,default="place")
    email=models.EmailField(max_length=100,unique=True)
    address=models.TextField(default="address")
    mobile=models.CharField(max_length=100,default="phone")
    date_join=models.DateField(null=True)
    eduqu=models.CharField(max_length=100,default="qualification")
    userRole=models.CharField(max_length=100,default='admin')
    username=models.CharField(max_length=100,default="username")
    password=models.CharField(max_length=100,default="password")
    conpass=models.CharField(max_length=100,default="confirm password")
    dummy1=models.CharField(max_length=100,default="dummy1")
    dummy2=models.CharField(max_length=100,default="dummy2")
    dummy3=models.CharField(max_length=100,default="dummy3")
    dummy4=models.CharField(max_length=100,default="dummy4")
    key = models.CharField(max_length=500, default="key")


class History(models.Model):
    id=models.AutoField(primary_key=True)
    modelname=models.CharField(max_length=100)
    savedid=models.CharField(max_length=100)
    operationdone=models.CharField(max_length=100)
    donebyuser=models.CharField(max_length=100)
    donebyUserRole=models.CharField(max_length=100)
    doneDateTime=models.DateTimeField(max_length=100)
    
    def __str__(self):
        return self.donebyuser
    
    