from .models import Option
from rest_framework import serializers

class OptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Option
        fields = ("text")
        
