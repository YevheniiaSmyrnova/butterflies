"""
Exhibition serializers module
"""
from rest_framework import serializers

from exhibition.models import Collection, Exhibition


class CollectionSerializer(serializers.ModelSerializer):
    """
    Collection serializer
    """
    class Meta:
        """
        Meta params
        """
        model = Collection


class ExhibitionSerializer(serializers.ModelSerializer):
    """
    Exhibition serializer
    """
    class Meta:
        """
        Meta params
        """
        model = Exhibition
