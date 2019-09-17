from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('dashboard/', views.dashboard, name='dashboard'),
  path('dashboard/create/', views.TeamCreate.as_view(), name='create_team'),
  path('dashboard/index/', views.team_index, name='index'),
  path('dashboard/team_detail/', views.team_detail, name='team_detail'),
#   path('dashboard/detail/', views.detail, name='detail'),
#   path('dashboard/<int:pk>/update/', views.DreamUpdate.as_view(), name='updateteam'),
  path('accounts/signup/', views.signup, name='signup'),
]

