from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets, status
from .serializers import *
from .models import *


class AddUserViewset(viewsets.ModelViewSet):
    queryset = Add_user.objects.all()
    serializer_class = Add_userSerializer


class CoordViewset(viewsets.ModelViewSet):
    queryset = Coord.objects.all()
    serializer_class = CoordSerializer


class LevelViewset(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ImagesViewset(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class PerevalViewset(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    def list_sd(self, request, *args, **kwargs):
        return Response({'message': 'Заполните поля и отправьте данные на сервер'})

    def create(self, request, *args, **kwargs):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            pereval_add = PerevalAdded.objects.create(raw_data=serializer.data)
            resp = Response(serializer.data, status=status.HTTP_200_OK)
            msg_resp = f"'status': '{resp.status_code}', 'message': '{resp.status_text}', 'id': '{pereval_add.id}'"
            return Response(msg_resp)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PerevalAddedViewset(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'pereval': reverse('pereval', request=request, format=format),
    })
