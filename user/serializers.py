from dataclasses import fields
from rest_framework import serializers
from user.models import UserProfile, User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password", "groups", "user_permissions")



class UserProfileSerializers(serializers.ModelSerializer):
    user = UserSerializers()

    class Meta:
        model = UserProfile
        fields = '__all__'
        