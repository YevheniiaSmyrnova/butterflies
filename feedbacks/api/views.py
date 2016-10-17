"""
Feedback api views module
"""
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from feedbacks.api.serializers import FeedbackSerializer
from feedbacks.models import Feedback


class FeedbackListCreateAPIView(ListCreateAPIView):
    """
    Feedback List and Create.
    The request is authenticated as a user, or is a read-only request.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class FeedbackRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update and Destroy feedback.
    The request is authenticated as a user, or is a read-only request.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(
            instance=instance, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=HTTP_400_BAD_REQUEST)
        instance = serializer.save()
        response = FeedbackSerializer(instance=instance).data
        return Response(status=HTTP_200_OK, data=response)
