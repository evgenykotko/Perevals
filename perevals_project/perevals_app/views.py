import django_filters
from django.http import Http404
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets, status, generics
from rest_framework.views import APIView

from .serializers import *
from .models import *


class PerevalListView(generics.ListAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer

class PerevalCreateView(generics.CreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddSerializer

class PerevalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddSerializer


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser

class UserFilter(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email']
