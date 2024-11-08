from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Jobs(models.Model):  # Inherit from models.Model here
    is_available = models.BooleanField(default=True)
    job_title = models.CharField(max_length=50)
    job_description = models.CharField(max_length=500)
    deal_payment = models.IntegerField(default=0)
    location = models.CharField(max_length=100)
    working_day = models.IntegerField(default=0)
    working_hours = models.IntegerField(default=0)
    experience_year = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)

    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
