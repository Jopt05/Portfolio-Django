from django.db import models

# Create your models here.


class Technology(models.Model):
    """ Projects i've used """

    tech_name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.tech_name
