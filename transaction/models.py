from django.db import models
from equipment.models import Equipment
from user.models import User

# Create your models here.
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    checkout_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Out')  # e.g., Out, Returned

    def __str__(self):
        return f"{self.equipment.name} - {self.user.username}"