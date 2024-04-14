from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.CharField(max_length=50)
    unit = models.ForeignKey('Unit', on_delete=models.SET_NULL, null=True)

class Unit(models.Model):
    name = models.CharField(max_length=100)
    uic = models.CharField(max_length=10)

    def __str__(self):
        return self.name

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
    serial_number = models.CharField(max_length=100)
    location = models.CharField(max_length = 25)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default='Available')  # e.g., Available, Signed out to X user 

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
    

class Cart(models.Model): 
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    equipment = models.ManyToManyField(Equipment, through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    Equipment= models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE)  # Assuming 'Equipment' is in the same app
    checkout_date = models.DateTimeField(auto_now_add=True)  # Use DateTimeField if time is relevant
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    
    # Correct status choices definition
    STATUS_CHOICES = [
        ('signed_out', 'Signed Out'),
        ('returned', 'Returned')
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='signed_out')

    def save(self, *args, **kwargs):
        if self.status == 'returned' and not self.actual_return_date:
            self.actual_return_date = timezone.now()  # Call the method to get the actual datetime
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.equipment.name} - {self.status}"