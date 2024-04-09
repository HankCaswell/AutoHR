from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Unit
from .models import Equipment
from .models import Transaction


class UserProfileSerializer(serializers.ModelSerializer):
    unit = serializers.PrimaryKeyRelatedField(queryset=Unit.objects.all(), allow_null=True)
    # Alternatively, if you want to use UIC as a reference:
    # unit_uic = serializers.SlugRelatedField(slug_field='uic', queryset=Unit.objects.all(), source='unit', allow_null=True)

    class Meta:
        model = UserProfile
        fields = ['rank', 'unit']

class UserRegistrationSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        UserProfile.objects.create(user=user, **profile_data)
        return user

class UnitSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Unit
        fields = ['id', 'name', 'uic']

class EquipmentSerialiers(serializers.ModelSerializer):
    user = UserRegistrationSerializer(read_only = True)
    equipment = serializers.SlugRelatedField(queryset = Equipment.objects.all(), slug_field = 'name')
    
    
    class Meta: 
        model = Transaction
        fields = ['user', 'equipment', 'checkout_date', 'return_date', 'status']


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Equipment
        fields = ['id', 'name', 'nsn', 'lin', 'unit', 'serial_number', 'status', 'location']