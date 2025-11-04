from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    number = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    course = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    session = models.CharField(max_length=30)
    address = models.TextField(max_length=255)
    pic = models.FileField(max_length=155,upload_to="student")
    regdate = models.DateField(max_length=30,auto_now_add=True)

class Login(models.Model):
    email = models.CharField(max_length=50,unique=True)
    password =models.CharField(max_length=50)

class Admin(models.Model):
    email = models.CharField(max_length=50,unique=True)
    password =models.CharField(max_length=50)

class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    message = models.TextField(max_length=255)



