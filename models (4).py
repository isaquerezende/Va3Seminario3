from django.db import models

# Create your models here.
class DetalheTurma(models.Model):
    aluno = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    turma = models.CharField(max_length=100)