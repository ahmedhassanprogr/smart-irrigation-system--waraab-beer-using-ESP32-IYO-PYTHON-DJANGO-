from django.shortcuts import render

# Create your views here.

from sensors.models import SensorData
from devices.models import PumbStatus



def dashboard(request):
    latest_sensor_data = SensorData.objects.order_by('-created_at').first()

    pumb_status = PumbStatus.objects.first()

    context = {
        'latest_sensor_data': latest_sensor_data,
        'pumb_status': pumb_status,

    }
    return render(request, 'home.html', context)