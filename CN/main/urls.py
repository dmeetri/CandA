from django.urls import path

from . import views

urlpatterns = [
    path('users/list', views.UsersListView.as_view(), name='userslist'),

    path('files/create/', views.FileCreateView.as_view(), name='filescreate'),
    path('files/list/', views.FilesListView.as_view(), name='fileslist'),
    path('files/detail/<int:pk>/', views.FileDetailView.as_view(), name='filesdetail'),
    path('files/update/<int:pk>/', views.FileUpdateView.as_view(), name='filesupdate'),
    path('files/delete/<int:pk>/', views.FileDeleteView.as_view(), name='filesdelete'),
]