from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.CharField(max_length=50)
    unit = models.ForeignKey('unit.Unit', on_delete=models.SET_NULL, null=True)