from rest_framework import viewsets
from .models import DetalheTurma
from DetalheTurma import detalheturmaserializers

class DetalheTurmaViews(viewsets.ModelViewSet):
    
    queryset = DetalheTurma.objects.all()
    serializer_class = detalheturmaserializers