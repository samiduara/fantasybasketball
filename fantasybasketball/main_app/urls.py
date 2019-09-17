from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('dashboard/', views.dashboard, name='dashboard'),
  path('accounts/signup/', views.signup, name='signup'),
  path('dashboard/create/', views.create_team, name='create_team'),
  path('dashboard/add_team/', views.add_team, name='add_team'),
]

