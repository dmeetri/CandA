from django.urls import path

from . import views

urlpatterns = [
    path('groups/create', views.GroupCreateView.as_view(), name='groupscreate'),
    path('groups/list', views.GroupListView.as_view(), name='groupslist'),
    path('groups/delete/<int:pk>', views.GroupDeleteView.as_view(), name='groupsdelete'),

    path('users/list', views.UsersListView.as_view(), name='userslist'),
    path('users/profile/<int:pk>/', views.UsersDetailView.as_view(), name='usersprofile'),

    path('files/create/', views.FileCreateView.as_view(), name='filescreate'),
    path('files/list/', views.FilesListView.as_view(), name='fileslist'),
    path('files/detail/<int:pk>/', views.FileDetailView.as_view(), name='filesdetail'),
    path('files/update/<int:pk>/', views.FileUpdateView.as_view(), name='filesupdate'),
    path('files/delete/<int:pk>/', views.FileDeleteView.as_view(), name='filesdelete'),
    path('files/delete/selected/', views.FilesDeleteSelectedView.as_view(), name='filesdeleteselected')
]