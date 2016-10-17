from rest_framework import serializers

from collector.models import Collector


class CollectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collector
