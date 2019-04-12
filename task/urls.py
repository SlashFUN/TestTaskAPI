from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('groups/', views.GroupListView.as_view(), name='group_list'),
    # path('users/<int:pk>', views.UserDetailView.as_view(), name='user_detail'),
    # path('groups/<int:pk>', views.GroupDetailView.as_view(), name='group_detail'),

    path('users/create', views.UserCreate.as_view(), name='user_create'),
    path('users/<int:pk>/edit', views.UserEdit.as_view(), name='user_edit'),
    path('users/<int:pk>/delete', views.UserDelete.as_view(), name='user_delete'),

    path('groups/create', views.GroupCreate.as_view(), name='group_create'),
    path('groups/<int:pk>/edit', views.GroupEdit.as_view(), name='group_edit'),
    path('groups/<int:pk>/delete', views.GroupDelete.as_view(), name='group_delete'),
]
