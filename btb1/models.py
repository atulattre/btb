from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')

class User1(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    
    firstname = models.CharField(max_length=100,null=False)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    student_id=models.IntegerField(default=0)
    phone=models.IntegerField()
    course = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    
    year=models.IntegerField(default=0)
    def __str__(self):
        return str(self.username)


class Rd(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    building_name = models.CharField(max_length=100)
    
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    space=models.IntegerField(default=0)
    images = models.ManyToManyField(Image)
    comments = models.CharField(max_length=255, default='Add description')
    def __str__(self):
        return str(self.username)
    


    
    