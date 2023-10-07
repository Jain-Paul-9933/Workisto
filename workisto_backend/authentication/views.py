from django.shortcuts import render
from rest_framework import generics
from authentication.models import CustomUser,UserProfile,WorkerProfile
from authentication.serializers import UserSerializer,MyTokenObtainPairSerializer,UserProfileSerializer,WorkerProfileSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.views import TokenObtainPairView

class UserRegistrationView(generics.CreateAPIView):

    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer
    permission_classes=(AllowAny,)

    def perform_create(self, serializer):
        
        user = serializer.save()

        password = serializer.validated_data.get('password')
        hashed_password = make_password(password)
        user.password=hashed_password
        
        
        if user.is_staff == False and user.is_superuser == False:
            UserProfile.objects.create(user=user)
            user.save()
        elif user.is_staff == True and user.is_superuser == False:
            WorkerProfile.objects.create(user=user)
            user.save()
        else:
            user.save()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer



class UserProfileView(generics.RetrieveUpdateAPIView):

    serializer_class=UserProfileSerializer
    permission_classes=(IsAuthenticated,)
    
    try:
        def get_object(self):
            return self.request.user.userprofile
    except:
        print("User Profile not found")

class WorkerProfileView(generics.RetrieveUpdateAPIView):

    serializer_class=WorkerProfileSerializer
    permission_classes=(IsAuthenticated,)
 
    try:
        def get_object(self):
            return self.request.user.workerprofile
    except:
        print("Worker Profile not found")
    

