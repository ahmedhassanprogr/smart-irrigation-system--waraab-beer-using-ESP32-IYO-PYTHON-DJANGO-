from django.shortcuts import render

# Create your views here.


from .models import PumbStatus
from .serializers import PumbStatusSerializer

from rest_framework.views import APIView
from rest_framework.response import Response    

class PumbStatusViewSet(APIView):
    def get(self, request):

        pumb = PumbStatus.objects.first()

    
        if not pumb:
          pumb = PumbStatus.objects.create(pumb_on=False)

        serializer = PumbStatusSerializer(pumb)
        return Response(serializer.data)
    
    def post(self, request):
        pumb = PumbStatus.objects.first()

        if not pumb:
            pumb = PumbStatus.objects.create()

        pumb.pumb_on = request.data.get('pumb_on',False)
        pumb.save()

        serializer = PumbStatusSerializer(pumb)
        return Response(serializer.data)





    
