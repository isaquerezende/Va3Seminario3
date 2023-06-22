from rest_framework import serializers
from Disciplina.models import Disciplina

class DisciplinaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = [
            'nome',
            'codigo ',
        ]
