from django.shortcuts import render
from rest_framework import generics
from .models import Painting
from .serializers import PaintingSerializer


class PaintingList(generics.ListCreateAPIView):
    serializer_class = PaintingSerializer

    def get_queryset(self):
        queryset = Painting.objects.all()

        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(title__icontains=title)

        date = self.request.query_params.get('date', None)
        if date is not None:
            queryset = queryset.filter(date__year=date)

        media = self.request.query_params.get('media', None)
        if media is not None:
            queryset = queryset.filter(media__icontains=media)

        height_min = self.request.query_params.get('height_min', None)
        if height_min is not None:
            queryset = queryset.filter(height__gte=height_min)

        height_max = self.request.query_params.get('height_max', None)
        if height_max is not None:
            queryset = queryset.filter(height__lte=height_max)

        width_min = self.request.query_params.get('width_min', None)
        if width_min is not None:
            queryset = queryset.filter(width__gte=width_min)

        width_max = self.request.query_params.get('width_max', None)
        if width_max is not None:
            queryset = queryset.filter(width__lte=width_max)

        price_min = self.request.query_params.get('price_min', None)
        if price_min is not None:
            queryset = queryset.filter(price__gte=price_min)

        price_max = self.request.query_params.get('price_max', None)
        if price_max is not None:
            queryset = queryset.filter(price__lte=price_max)

        return queryset


class PaintingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer
