from django.db import models

# Create your models here.


class Service(models.Model):
    """ Services I offer """
    SERVICE_TOPICS = (
        ('0', 'Web'),
        ('1', 'Coding')
    )

    service_name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    service_description = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    service_topic = models.CharField(
        max_length=1,
        null=False,
        blank=False,
        choices=SERVICE_TOPICS
    )
    service_image = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.service_name
