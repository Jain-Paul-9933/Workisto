from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('users_list/',views.UserListView.as_view(),name='users_list'),
    path('workers_list/',views.WorkerListView.as_view(),name='workers_list'),
]
