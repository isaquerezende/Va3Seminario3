from rest_framework import serializers
from Alunos.models import Alunos

class AlunosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alunos
        fields = [
            'nome',
            'sexo ',
            'registro',
        ]

