from rest_framework import serializers
from user.models import UserProfile, User
from blog.serializers import ArticleSerializers


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password", "groups", "user_permissions")



class UserProfileSerializers(serializers.ModelSerializer):
    user = UserSerializers()
    article_set = ArticleSerializers(many=True)

    class Meta:
        model = UserProfile
        fields = '__all__'
        