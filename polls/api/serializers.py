"""
Polls serializers module
"""
from rest_framework import serializers

from polls.models import Question, Choice


class QuestionSerializer(serializers.ModelSerializer):
    """
    Question serializer
    """
    class Meta:
        """
        Meta params
        """
        model = Question


class ChoiceSerializer(serializers.ModelSerializer):
    """
    Choice serializer
    """
    class Meta:
        """
        Meta params
        """
        model = Choice
