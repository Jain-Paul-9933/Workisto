from rest_framework import serializers
from .models import CustomUser,UserProfile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password',
                  'phone_number', 'is_active', 'is_staff', 'is_superuser')

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):

        token = super().get_token(user)

        token['user']={
            'username':user.username,
            'email':user.email,
            'password':user.email,
            'phone_number':user.password,
            'is_active':user.is_active,
            'is_staff':user.is_staff,
            'is_superuser':user.is_superuser,
        }
        
        return token
    

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields='__all__'