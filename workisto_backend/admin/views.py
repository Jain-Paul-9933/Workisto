from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics
from authentication.models import CustomUser
from authentication.serializers import UserSerializer
from .permissions import IsSuperuser

class UserListView(generics.ListAPIView):
    serializer_class=UserSerializer
    permission_classes=(IsSuperuser,)

    def get_queryset(self):
        return CustomUser.objects.filter(Q(is_staff=False)&Q(is_superuser=False))


class WorkerListView(generics.ListAPIView):
    serializer_class=UserSerializer
    permission_classes=(IsSuperuser,)

    def get_queryset(self):
        return CustomUser.objects.filter(Q(is_staff=True)&Q(is_superuser=False))