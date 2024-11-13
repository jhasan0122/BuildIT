# Generated by Django 5.1.1 on 2024-11-11 03:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "project_manage",
            "0003_project_has_accepted_project_project_description_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="proposed_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
