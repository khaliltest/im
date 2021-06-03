
from .models import Image
from rest_framework import serializers

class ImSer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
