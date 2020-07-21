from django.shortcuts import render
from rest_framework import generics
from .models import Painting
from .serializers import PaintingSerializer


class PaintingList(generics.ListCreateAPIView):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer


class PaintingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer
