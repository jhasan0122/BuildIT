from django.db import models
from django.utils import timezone
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class HirePost(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expart_type = models.CharField(max_length=50)
    phone = models.CharField(max_length=15,default='0000000000')
    description = models.TextField()
    offered_money = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

