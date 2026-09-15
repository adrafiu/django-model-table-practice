from django.db import models


# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Students(models.Model):
    name = models.CharField(max_length=100, verbose_name="Student Full Name")
    email = models.EmailField()
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"
