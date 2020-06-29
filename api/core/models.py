from django.db import models

# Create your models here.
class Document(models.Model):
    date = models.DateTimeField(auto_now=True)
    archive = models.FileField(upload_to="files/",blank=True,null=True)

class Recomendation(models.Model):
    word = models.CharField(max_length=50)
    recomendations =  models.TextField()   

