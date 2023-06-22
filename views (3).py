from rest_framework import viewsets
from .models import DetalheDisciplina
from DetalheDisciplina import detalhedisciplinaserializers

class DetalheDisciplinaViews(viewsets.ModelViewSet):
    
    queryset = DetalheDisciplina.objects.all()
    serializer_class = detalhedisciplinaserializers
