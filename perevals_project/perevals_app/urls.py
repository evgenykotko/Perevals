from django.urls import path
from . import views
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

submitData = PerevalAddedViewset.as_view({
    'get': 'retrieve',
    'post': 'create',
    'patch': 'partial_update'
})

pereval = PerevalAddedViewset.as_view({
    'get': 'list'
})

pereval_details = PerevalAddedViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', views.api_root),
    path('pereval/submitData/', submitData, name='submitData'),
    path('pereval/submitData/<int:pk>', submitData, name='submitData'),
    path('pereval/', pereval, name='pereval'),
    path('pereval/<int:pk>/', pereval_details, name='pereval_details'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
