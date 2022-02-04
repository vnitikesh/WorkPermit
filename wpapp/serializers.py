from rest_framework import serializers
from .models import *

class WorkPermitSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPermit
        fields = '__all__'

class ExampleWorkPermitSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkpermitExample
        fields = '__all__'