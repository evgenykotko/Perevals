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

    def create(self, request, *args, **kwargs):
        serializer = PerevalAddedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            resp = Response(serializer.data, status=status.HTTP_200_OK)
            print(dict(serializer.data))
            msg_resp = f"'status': '{resp.status_code}', 'message': '{resp.status_text}', 'id': '{dict(serializer.data).get('id')}'"
            return Response(msg_resp)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'pereval': reverse('pereval', request=request, format=format),
    })
