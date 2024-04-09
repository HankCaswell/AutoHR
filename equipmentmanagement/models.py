from django.db import models
from django.contrib.auth.models import User
from django.db import models
from .models import Equipment

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.CharField(max_length=50)
    unit = models.ForeignKey('unit.Unit', on_delete=models.SET_NULL, null=True)

class Unit(models.Model):
    name = models.CharField(max_length=100)
    uic = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    checkout_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Out')  # e.g., Out, Returned

    def __str__(self):
        return f"{self.equipment.name} - {self.user.username}"

class Equipment(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('maintenance', 'Maintenance'),
        ('turn-in', 'Turn-in')
    )
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='equipments')
    name = models.CharField(max_length=100)
    nsn = models.CharField(max_length = 20, blank = True, null = True)
    lin = models.CharField(max_length=50, blank = True, null = True)
    serial_number = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length = 25)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default='Available')  # e.g., Available, Signed out to X user 

    def __str__(self):
        return self.name