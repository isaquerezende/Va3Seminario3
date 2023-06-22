from rest_framework import serializers
from DetalheCurso.models import DetalheCurso

class DetalheCursoSerializers(serializers.ModelSerializer):
    class Meta:
        model = DetalheCurso
        fields = [
            'nome',
            'codigo',
        ]

