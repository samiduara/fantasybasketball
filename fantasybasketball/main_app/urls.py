from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('', views.dashboard, name='dashboard'),
  path('accounts/signup/', views.signup, name='signup'),
]