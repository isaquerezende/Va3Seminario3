from rest_framework import serializers
from Curso.models import Curso

class CursoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = [
            'nome',
            'codigo ',
        ]
