from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
from unit.models import Unit

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