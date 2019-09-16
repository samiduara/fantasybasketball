from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('dashboard/', views.dashboard, name='dashboard'),
  path('accounts/signup/', views.signup, name='signup'),
  path('dashboard/create/', views.DreamCreate.as_view(), name='dreamteam'),
]

