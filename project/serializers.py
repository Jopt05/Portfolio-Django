from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """ Serializer de proyectos """

    class Meta:
        model = Project
        fields = (
            'project_name',
            'project_description',
            'project_technologies',
            'project_url',
            'project_topic',
        )
