from django.db import models

# Create your models here.

class Student(models.Model):

    std_id = models.IntegerField()
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    phone = models.CharField(max_length=10)

