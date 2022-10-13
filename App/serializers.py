from rest_framework import serializers
from App.models import prepaid,postpaids


class prepaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = prepaid
        fields = '__all__'

class postpaidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = postpaids
        fields = '__all__'