# Generated by Django 5.1.1 on 2024-11-19 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_project_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]