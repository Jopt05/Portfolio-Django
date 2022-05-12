from django.db import models

from technology.models import Technology
# Create your models here.


class Project(models.Model):
    """ Projects i've done """
    project_name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    project_description = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    project_technologies = models.ManyToManyField(
        Technology
    )
    project_url = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.project_name
