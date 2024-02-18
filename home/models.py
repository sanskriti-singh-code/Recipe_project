from django.db import models

# Create your models here.
class student(models.Model):
    # id=models.autofield() default created by django act as primary key
    name = models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField(null=True, blank=True)
    image=models.ImageField(null=True,blank=True)
    # file=models.FileField()

class product(models.Model):
    pass

class car(models.Model):
    car_name=models.CharField( max_length=500)
    speed=models.IntegerField(default=50)
    