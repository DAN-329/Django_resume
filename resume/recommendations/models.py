from django.db import models

# Create your models here.
class Record(models.Model):
    name=models.CharField(max_length=20)
    position=models.CharField(max_length=20)
    number=models.IntegerField()
    Email=models.CharField(max_length=30)
    Company=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Test(models.Model):

    name = models.CharField(max_length=10)
    position=models.CharField(max_length=20)
    #number=models.IntegerField()
    Email=models.CharField(max_length=30)

 