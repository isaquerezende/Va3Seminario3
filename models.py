from django.db import models

# Create your models here.
class Alunos(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    registro = models.IntegerField()

   