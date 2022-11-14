from rest_framework import serializers
from .models import Phones


class PhonesSerial(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    surname = serializers.CharField(max_length=50)
    number = serializers.CharField(max_length=50)

    class Meta:
        model = Phones
        fields = ('id', 'name', 'surname', 'number')