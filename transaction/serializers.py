from rest_framework import serializers
from .models import Transaction
from user.serializers import UserSerializer
from equipment.models import Equipment

class EquipmentSerialiers(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    equipment = serializers.SlugRelatedField(queryset = Equipment.objects.all(), slug_field = 'name')
    
    
    class Meta: 
        model = Transaction
        fields = ['user', 'equipment', 'checkout_date', 'return_date', 'status']