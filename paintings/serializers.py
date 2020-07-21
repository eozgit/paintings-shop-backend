from rest_framework import serializers
from .models import Painting


class PaintingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Painting
        fields = ('id', 'title', 'date', 'media',
                  'height', 'width', 'imageUrl',)
