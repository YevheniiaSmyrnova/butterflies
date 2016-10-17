from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from collector.api.serializers import CollectorSerializer
from collector.models import Collector


class CollectorListCreateAPIView(ListCreateAPIView):
    queryset = Collector.objects.all()
    serializer_class = CollectorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CollectorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Collector.objects.all()
    serializer_class = CollectorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

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
