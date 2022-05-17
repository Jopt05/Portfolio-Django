from rest_framework.views import APIView
from django.http import JsonResponse

from .serializers import ProjectSerializer
from .models import Project
# Create your views here.


class ProjectAPIView(APIView):

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)

        return JsonResponse({
            "status": "ok",
            "services": serializer.data
        })
