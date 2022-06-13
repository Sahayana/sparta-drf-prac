from django.urls import path
from blog.views import ArticleCreateView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', csrf_exempt(ArticleCreateView.as_view())),
    
]

