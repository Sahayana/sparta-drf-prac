from django.urls import path
from user.views import UserApiView, UserDetailView


urlpatterns = [
    path('login/', UserApiView.as_view()),
    path('detail/', UserDetailView.as_view())
]

