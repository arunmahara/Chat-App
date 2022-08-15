from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginUser, name='login'),
    path('home/', views.home, name='home'),
    path('signup', views.signupUser, name='signup'),
    path('logout/', views.logoutUser, name='logout'),
]
