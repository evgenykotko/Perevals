from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

# pereval_list = PerevalViewSet.as_view({'get': 'list'})
# pereval_detail = PerevalViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    path('', PerevalListView.as_view()),
    path('submitData/', PerevalCreateView.as_view()),
    path('submitData/<int:pk>/', PerevalDetailView.as_view()),
    path('user/', UserView.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),
    path('user/?email=<email>/', UserFilter.as_view())
]
