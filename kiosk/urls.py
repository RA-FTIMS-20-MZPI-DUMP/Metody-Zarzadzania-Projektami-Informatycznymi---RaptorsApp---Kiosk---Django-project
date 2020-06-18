from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('robot_dismiss', views.robot_dismiss, name = 'robot_dismiss'),
    path('select', views.kiosk_select, name = 'select'),
    path('home/<int:id>/', views.home, name = 'home'),
    path('poke', views.poke, name = 'poke'),
    path('data', views.data, name = 'data'),
    path('pomoc', views.pomoc, name = 'pomoc'),
    path('free', views.free, name = 'free'),
]
