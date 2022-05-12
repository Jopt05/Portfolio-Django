from django.http import JsonResponse

from .models import Service
# Create your views here.


def get_services(request):
    try:
        services = Service.objects.all().values()
        return JsonResponse({
            "status": "ok",
            "services": list(services)
        })
    except NameError:
        return JsonResponse({
            "status": "fail",
            "message": "Something went wrong"
        })
