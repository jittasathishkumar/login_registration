from django.db import models

# Create your models here.

class info(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Mobile=models.IntegerField()
    Address=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)




class issue(models.Model):

    Name=models.CharField(max_length=50)
    Mobile=models.IntegerField()
    concern=models.CharField(max_length=50)
    query=models.CharField(max_length=50)
    feedback=models.CharField(max_length=50)
    

