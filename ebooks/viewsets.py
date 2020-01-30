from rest_framework import viewsets
from . import models
from . import serializers


class AbooViewSets(viewsets.ModelViewSet):
    queryset = models.AbooMain.objects.all()
    serializer_class = serializers.AbooSerializer
