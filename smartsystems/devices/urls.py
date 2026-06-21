from django.urls import path
from .views import PumbStatusViewSet

urlpatterns = [
    path('pumb/', PumbStatusViewSet.as_view(), name='pumb-status'),
]