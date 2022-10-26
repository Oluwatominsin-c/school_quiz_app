# from distutils.command.upload import upload
from django.db import models
# from django.forms import CharField

# Create your models here.

class Quiz(models.Model):
    name = models.CharField(max_length=30)
    number_of_question = models.IntegerField(default=30)
    image = models.ImageField(upload_to="images/")

    def __str__(self) -> str:
        return self.name

class Phy101(models.Model):
    question = models.CharField(max_length=1000)
    option1 = models.CharField(max_length=1000)
    option2 = models.CharField(max_length=1000)
    option3 = models.CharField(max_length=1000)
    option4 = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000)
