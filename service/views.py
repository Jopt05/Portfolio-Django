from rest_framework.views import APIView
from django.http import JsonResponse

from service.serializers import ServiceSerializer
from .models import Service
# Create your views here.


class ServiceAPIView(APIView):

    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)

        return JsonResponse({
            "status": "ok",
            "services": serializer.data
        })
