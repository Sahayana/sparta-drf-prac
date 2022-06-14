from rest_framework import serializers
from user.models import UserProfile, User
from blog.serializers import ArticleSerializers


class UserSerializers(serializers.ModelSerializer):
    article_set =   ArticleSerializers(many=True)

    class Meta:
        model   =   User
        exclude =   ("groups", "user_permissions")
        extra_kwargs    =   {
            "password": {"write_only": True}
        }



class UserProfileSerializers(serializers.ModelSerializer):
    user        =   UserSerializers()    

    class Meta:
        model   =   UserProfile
        fields  =   '__all__'
        