from rest_framework import serializers
from .models import AbooMain


class AbooSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbooMain
        fields = '__all__'
