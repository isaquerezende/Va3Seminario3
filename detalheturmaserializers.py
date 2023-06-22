from rest_framework import serializers
from DetalheTurma.models import DetalheTurma

class DetalheTurmaSerializers(serializers.ModelSerializer):
    class Meta:
        model = DetalheTurma
        fields = [
            'aluno',
            'professor',
            'turma',
        ]

