from django.shortcuts import render
from rest_framework import generics
from authentication.models import CustomUser,UserProfile
from authentication.serializers import UserSerializer,MyTokenObtainPairSerializer,UserProfileSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.views import TokenObtainPairView

class UserRegistrationView(generics.CreateAPIView):

    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer
    permission_classes=(AllowAny,)

    def perform_create(self, serializer):
        
        password = serializer.validated_data.get('password')

        hashed_password = make_password(password)

        serializer.save(password=hashed_password)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):

    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer
    permission_classes=(IsAuthenticated,)