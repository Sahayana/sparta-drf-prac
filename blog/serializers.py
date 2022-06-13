from rest_framework import serializers
from blog.models import Article




class ArticleSerializers(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Article
        fields = "__all__"