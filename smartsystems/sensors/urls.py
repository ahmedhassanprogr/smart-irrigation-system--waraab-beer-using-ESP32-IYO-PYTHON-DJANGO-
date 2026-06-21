from django.urls import path
from .views import SensorDataViewSet 

urlpatterns = [
    path('sensors/', SensorDataViewSet.as_view(), name='sensor-data'),
]