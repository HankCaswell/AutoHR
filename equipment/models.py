from django.db import models
from unit.models import Unit


# Create your models here.
class Equipment(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('maintenance', 'Maintenance'),
        ('turn-in', 'Turn-in')
    )
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='equipments')
    name = models.CharField(max_length=100)
    nsn = models.CharField(max_length = 20)
    lin = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length = 25)
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default='Available')  # e.g., Available, Signed out to X user 

    def __str__(self):
        return self.name