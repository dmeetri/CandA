from django.urls import path

from . import views

urlpatterns = [
    path('files/create/', views.FileCreateView.as_view(), name='filescreate'),
    path('files/', views.FilesListView.as_view(), name='files'),
]