# Generated by Django 4.0.4 on 2022-05-12 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_image',
            field=models.CharField(max_length=255),
        ),
    ]
