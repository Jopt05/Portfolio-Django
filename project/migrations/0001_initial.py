# Generated by Django 4.0.4 on 2022-05-12 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_description', models.CharField(max_length=255)),
                ('project_technology', models.CharField(choices=[('0', 'HTML'), ('1', 'CSS'), ('2', 'Javascript'), ('3', 'React'), ('4', 'Python')], max_length=1)),
                ('project_url', models.CharField(max_length=255)),
            ],
        ),
    ]
