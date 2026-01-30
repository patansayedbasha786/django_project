from django.db import models

# Create your models here.


class student(models.Model):
    student_name=models.CharField(max_length=10)
    roll=models.IntegerField(max_length=10)
    branch=models.CharField(max_length=10)

def __str__(self):
    return self.name

