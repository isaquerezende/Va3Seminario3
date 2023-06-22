from rest_framework import viewsets
from .models import DetalheCurso
from DetalheCurso import detalhecursoserializers

class DetalhecursoViews(viewsets.ModelViewSet):
    
    queryset = DetalheCurso.objects.all()
    serializer_class = detalhecursoserializers
