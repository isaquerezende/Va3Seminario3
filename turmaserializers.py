from rest_framework import serializers
from Turma.models import Turma

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = [
            'curso',
            'codigo',
        ]

