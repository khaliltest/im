from django.shortcuts import render
from .models import Image
from .serializers import ImSer
from rest_framework import generics

class createImage(generics.CreateAPIView):
    serializer_class = ImSer
    queryset = Image.objects.all()

