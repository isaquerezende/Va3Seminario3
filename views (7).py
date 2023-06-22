from rest_framework import viewsets
from .models import Turma
from Turma import turmaserializers

class TurmaView(viewsets.ModelViewSet):
    
    queryset = Turma.objects.all()
    serializers_class = turmaserializers