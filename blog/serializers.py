from dataclasses import fields
from rest_framework import serializers
from blog.models import Article, Comment




class CommentSerializers(serializers.ModelSerializer):
    author      =   serializers.StringRelatedField()
    article     =   serializers.StringRelatedField()
    
    class Meta:
        model   =   Comment
        fields  =   "__all__"



class ArticleSerializers(serializers.ModelSerializer):
    author      =   serializers.StringRelatedField()
    category    =   serializers.StringRelatedField(many=True, read_only=True)
    comment_set =   CommentSerializers(many=True)

    class Meta:
        model   =   Article
        fields  =   "__all__"
