
from user.models import UserProfile, User
from user.permissions import IsPublicPermission
from blog.models import Article, Category
from blog.serializers import ArticleSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


class ArticleCreateView(APIView):
    permission_classes = [IsPublicPermission]   
    
    def post(self, request):     
        
        data = {
            "author" : User.objects.get(id=request.data.get("author_id")),
            "title" : request.data.get("title"),
            "content" : request.data.get("content"),
            }
        category = request.data.get("category")

        article = Article.objects.create(**data)

        if not Category.objects.filter(name = category).exists():
            return Response({"error":"UNKNOWN_CATEGORY"}, status=status.HTTP_404_NOT_FOUND)

        article.category.add(Category.objects.get(name=category))
        
        serializer = ArticleSerializers(article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
       
        
        
