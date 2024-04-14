from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Unit
from .models import Equipment
from .models import Transaction
from rest_framework.generics import get_object_or_404



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('rank', 'unit')  # Specify fields that make sense in your scenario

class UserRegistrationSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=True)
    unit_id = serializers.PrimaryKeyRelatedField(
        queryset=Unit.objects.all(),
        write_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'profile', 'unit_id')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        unit = validated_data.pop('unit_id')  # Directly pop 'unit_id' which should now be present

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Now directly use 'unit' from above to assign to the user profile
        UserProfile.objects.create(user=user, unit=unit, **profile_data)
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


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    # unit_id = serializers.IntegerField()
    # Alternatively, if you want to use UIC as a reference:
    # unit_uic = serializers.SlugRelatedField(slug_field='uic', queryset=Unit.objects.all(), source='unit', allow_null=True)                