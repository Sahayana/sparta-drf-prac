from django.contrib.auth import authenticate, login
from user.models import User, UserProfile
from user.serializers import UserProfileSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status, generics


# Create your views here.

class UserApiView(APIView):

    permission_classes  =   [permissions.AllowAny]
    
    def post(self, request):        
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "FAILED"}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "SUCCESS"}, status=status.HTTP_200_OK)

class UserDetailView(APIView):

    permission_classes  =   [permissions.AllowAny]

    def get(self, request):
        if not request.user.is_authenticated:
            return Response({"error": "AUTHENTICATION_FAILED"}, status=status.HTTP_401_UNAUTHORIZED)
        user = UserProfile.objects.select_related("user").get(user_id=request.user.id)
        data = UserProfileSerializers(user).data        
        return Response(data, status=status.HTTP_200_OK)
