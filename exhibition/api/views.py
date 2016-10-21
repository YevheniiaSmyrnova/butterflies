"""
Exhibition api views module
"""
from rest_framework import exceptions
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from exhibition.api.serializers import ExhibitionSerializer, \
    CollectionSerializer
from exhibition.models import Exhibition, Collection


class ExhibitionListCreateAPIView(ListCreateAPIView):
    """
    Exhibition List and Create.
    The request is authenticated as a user, or is a read-only request.
    """
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ExhibitionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update and Destroy exhibition.
    The request is authenticated as a user, or is a read-only request.
    """
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(
            instance=instance, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=HTTP_400_BAD_REQUEST)
        instance = serializer.save()
        response = ExhibitionSerializer(instance=instance).data
        return Response(status=HTTP_200_OK, data=response)


class CollectionListCreateAPIView(ListCreateAPIView):
    """
    Collection List and Create.
    The request is authenticated as a user, or is a read-only request.
    """
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        """
        Optionally restricts the returned collections,
        by filtering against a `name` query parameter in the URL.
        """
        queryset = super(CollectionListCreateAPIView, self).get_queryset()
        # queryset = Collection.objects.all()
        name = self.request.query_params.get('name', None)
        print(name)
        if name:
            queryset = queryset.filter(name=name)
        return queryset


class CollectionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update and Destroy collection.
    The request is authenticated as a user, or is a read-only request.
    """
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(
            instance=instance, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=HTTP_400_BAD_REQUEST)
        instance = serializer.save()
        response = CollectionSerializer(instance=instance).data
        return Response(status=HTTP_200_OK, data=response)
