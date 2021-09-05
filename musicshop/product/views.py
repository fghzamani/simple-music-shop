from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from product import serializers
from product.models import Track
from product.serializers import TrackSerializer,AlbumSerializer


class TrackView(GenericViewSet):
    @action(methods=['GET'], detail=False, url_name='unit1', url_path='unit1')
    def unit1_track(self, request, *args, **kwargs):
        qs = Track.objects.filter(unit_price__gt=1)
        qs_ser = TrackSerializer(qs, many=True)
        return Response(data={'result': qs_ser.data}, status=200)

    @action(methods=['GET'], detail=False, url_name='all', url_path='all')
    def all_tracks(self, request, *args, **kwargs):
        qs = Track.objects.all()
        qs_ser = TrackSerializer(qs, many=True)
        return Response(data={'result': qs_ser.data}, status=200)


class AlbumView(GenericViewSet):
    @action(methods=['POST'],
            detail=False, url_name='albumImage',
            url_path='albumImage',
            serializer_class=serializers.AlbumSerializer)
    def create_album(self, request, *args, **kwargs):
        in_serializer = serializers.AlbumSerializer(data=request.data)
        in_serializer.is_valid(raise_exception=True)
        in_serializer.save()

        return Response(data={"meta": {"success": True, "code": 201, }, "result": in_serializer.data, })
