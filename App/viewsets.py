from rest_framework import viewsets

from App import serializers
from App.models import prepaid,postpaids


class prepaidViewSet(viewsets.ModelViewSet):
    queryset = prepaid.objects.all()
    serializer_class = serializers.prepaidSerializer

class postpaidsiewSet(viewsets.ModelViewSet):
    queryset = postpaids.objects.all()
    serializer_class = serializers.postpaidsSerializer