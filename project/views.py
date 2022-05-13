from django.http import JsonResponse

from .models import Project
# Create your views here.


def get_projects(request):
    try:
        response = []
        projects = Project.objects.all()
        for p in projects:
            project = {}
            project['project_name'] = p.project_name
            project['project_description'] = p.project_description
            project['project_technologies'] = list(
                p.project_technologies.all().values()
            )
            project['project_topic'] = p.project_topic
            project['project_url'] = p.project_url
            response.append(project)
        print(projects)
        return JsonResponse({
            "status": "ok",
            "projects": response
        })
    except NameError:
        return JsonResponse({
            "status": "fail",
            "message": "Something went wrong"
        })
