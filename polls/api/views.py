"""
Polls api views module
"""
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from polls.api.serializers import QuestionSerializer, \
    ChoiceSerializer
from polls.models import Question, Choice


class QuestionListCreateAPIView(ListCreateAPIView):
    """
    Questions List and Create.
    The request is authenticated as a user, or is a read-only request.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class QuestionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update and Destroy question.
    The request is authenticated as a user, or is a read-only request.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(
            instance=instance, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=HTTP_400_BAD_REQUEST)
        instance = serializer.save()
        response = QuestionSerializer(instance=instance).data
        return Response(status=HTTP_200_OK, data=response)


class ChoiceListCreateAPIView(ListCreateAPIView):
    """
    Choice List and Create.
    The request is authenticated as a user, or is a read-only request.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        """
        List of answers to the question
        :return:
        """
        queryset = Choice.objects.all()
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {'question': self.kwargs[lookup_url_kwarg]}
        return queryset.filter(**filter_kwargs)
