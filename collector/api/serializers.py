"""
Collector serializers module
"""
from rest_framework import serializers

from collector.models import Collector


class CollectorSerializer(serializers.ModelSerializer):
    """
    Collector serializer
    """
    class Meta:
        """
        Meta params
        """
        model = Collector
