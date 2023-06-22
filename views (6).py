from rest_framework import viewsets
from .models import Professor
from Professor import professorserializers

class ProfessorView(viewsets.ModelViewSet):
    
    queryset = Professor.objects.all()
    serializers_class = professorserializers
