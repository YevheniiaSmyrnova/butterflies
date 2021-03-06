"""
Collector api views module
"""
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, \
    IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from collector.api.serializers import CollectorSerializer
from collector.models import Collector


class CollectorListCreateAPIView(ListCreateAPIView):
    """
    Collector List and Create.
    The request is authenticated as a user, or is a read-only request.
    """
    queryset = Collector.objects.all()
    serializer_class = CollectorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CollectorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update and Destroy collector.
    The request is authenticated as a user, or is a read-only request.
    """
    queryset = Collector.objects.all()
    serializer_class = CollectorSerializer
    # permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(
            instance=instance, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=HTTP_400_BAD_REQUEST)
        instance = serializer.save()
        response = CollectorSerializer(instance=instance).data
        return Response(status=HTTP_200_OK, data=response)

    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned collections,
    #     by filtering against a `name` query parameter in the URL.
    #     """
    #     queryset = Collector.objects.all()
    #     surname = self.request.user.last_name
    #     if surname:
    #         queryset = queryset.filter(surname=surname)
    #     return queryset
