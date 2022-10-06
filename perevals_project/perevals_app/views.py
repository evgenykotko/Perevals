from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets, status
from .serializers import *
from .models import *


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CoordViewset(viewsets.ModelViewSet):
    queryset = Coord.objects.all()
    serializer_class = CoordSerializer


class LevelViewset(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class PerevalImagesViewset(viewsets.ModelViewSet):
    queryset = PerevalImages.objects.all()
    serializer_class = PerevalImagesSerializer


class PerevalAddedViewset(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer

    def list_sd(self, request, *args, **kwargs):
        return Response({'message': 'Заполните поля и отправьте данные на сервер'})

    def retrieve(self, request, pk=None):
        queryset = PerevalAdded.objects.all()
        pereval = get_object_or_404(queryset, pk=pk)
        serializer = PerevalAddedSerializer(pereval)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = PerevalAddedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            resp = Response(serializer.data, status=status.HTTP_200_OK)
            rsc = resp.status_code
            rct = resp.status_text
            pid = dict(serializer.data).get('id')
            msg_resp = f"'status': '{rsc}', 'message': '{rct}', 'id': '{pid}'"
            return Response(msg_resp)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'pereval': reverse('pereval', request=request, format=format),
    })
