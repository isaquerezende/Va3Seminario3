from rest_framework import serializers
from Professor.models import Professor

class ProfessorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = [
            'nome',
            'registro',
            'sexo',
        ]

