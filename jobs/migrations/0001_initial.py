# Generated by Django 5.1.1 on 2024-11-08 13:28

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Jobs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_available", models.BooleanField(default=True)),
                ("job_title", models.CharField(max_length=50)),
                ("job_description", models.CharField(max_length=500)),
                ("deal_payment", models.IntegerField(default=0)),
                ("location", models.CharField(max_length=100)),
                ("working_day", models.IntegerField(default=0)),
                ("working_hours", models.IntegerField(default=0)),
                (
                    "date_posted",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "posted_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
