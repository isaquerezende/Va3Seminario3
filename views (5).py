from rest_framework import viewsets
from .models import Disciplina 
from Disciplina import disciplinaserializer

class DisciplinaViews(viewsets.ModelViewSet):
    
    queryset = Disciplina.objects.all()
    serializers_class = disciplinaserializer

# Create your views here.
