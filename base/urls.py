from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='homepage'),
    path('room/<str:pk>/', views.room, name='roompage'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('deleteMessage/<str:pk>/', views.deleteMessage, name='delete-message'),
    # auth
    path('', views.loginPage, name='loginPage'),
    path('logoutPage', views.logoutPage, name='logout'),
    path('register', views.registerUser, name='register'),
    # create form
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name='updateRoom'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='deleteRoom'),

    path('update-user/', views.updateUser, name='update-user'),

]
