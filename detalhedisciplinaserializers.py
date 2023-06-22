from rest_framework import serializers
from DetalheDisciplina.models import DetalheDisciplina

class DetalheDisciplinaSerializers(serializers.ModelSerializer):
    class Meta:
        model = DetalheDisciplina
        fields = [
            'disciplina',
            'curso',
        ]

