from django.db import models

# Create your models here.


class Project(models.Model):
    """ Projects i've done """
    PROJECT_TECHNOLOGIES = (
        ('0', 'HTML'),
        ('1', 'CSS'),
        ('2', 'Javascript'),
        ('3', 'React'),
        ('4', 'Python'),
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
    project_technology = models.CharField(
        max_length=1,
        null=False,
        blank=False,
        choices=PROJECT_TECHNOLOGIES
    )
    project_url = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.project_name
