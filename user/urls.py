from django.contrib import admin
from django.urls import path
from user.views import UserApiView, UserDetailView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('login/', UserApiView.as_view()),
    path('detail/', UserDetailView.as_view())
]

