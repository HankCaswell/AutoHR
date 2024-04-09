from django.db import models

# Create your models here.
class Unit(models.Model):
    name = models.CharField(max_length=100)
    uic = models.CharField(max_length=10)

    def __str__(self):
        return self.name