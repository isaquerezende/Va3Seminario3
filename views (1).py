from rest_framework import viewsets
from .models import Curso
from Curso import cursoserializers

class CursoViews(viewsets.ModelViewSet):
    
    queryset = Curso.objects.all()
    serializers_class = cursoserializers
