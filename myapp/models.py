from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    age = models.PositiveIntegerField()
    
class Course(models.Model):
    title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    
class Students(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=100)
    address = models.TextField()
        
        
