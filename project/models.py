from django.db import models

from technology.models import Technology
# Create your models here.


class Project(models.Model):
    """ Projects i've done """

    PROJECT_TOPICS = (
        ('0', 'Game'),
        ('1', 'Code'),
        ('2', 'Web'),
        ('3', 'API'),
    )

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
    project_topic = models.CharField(
        max_length=1,
        null=False,
        blank=False,
        choices=PROJECT_TOPICS
    )

    def __str__(self):
        return self.project_name
