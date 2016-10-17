"""
Feedback serializers module
"""
from rest_framework import serializers

from feedbacks.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    """
    Feedback serializer
    """
    class Meta:
        """
        Meta params
        """
        model = Feedback
