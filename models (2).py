from django.db import models

# Create your models here.
class DetalheCurso(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)