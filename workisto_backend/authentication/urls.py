from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('user_registration/',views.UserRegistrationView.as_view(),name='user_registration'),
    path('auth_token/',views.MyTokenObtainPairView.as_view(),name='auth_token'),
    path('user_profile/',views.UserProfileView.as_view(),name='user_profile'),
    path('worker_profile/',views.WorkerProfileView.as_view(),name='worker_profile'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
