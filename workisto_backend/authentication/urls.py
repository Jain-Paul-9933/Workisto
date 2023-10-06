from django.urls import path
from .import views

urlpatterns = [
    path('user_registration/',views.UserRegistrationView.as_view(),name='user_registration'),
    path('auth_token/',views.MyTokenObtainPairView.as_view(),name='auth_token'),
]
