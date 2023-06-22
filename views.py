from rest_framework import viewsets
from .models import Alunos
from Alunos import alunosserializers

class AlunosViews(viewsets.ModelViewSet):
    
    queryset = Alunos.objects.all()
    serializer_class = alunosserializers
