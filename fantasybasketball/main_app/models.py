from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Player(models.Model):
  api_id=models.IntegerField()
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  user_name = models.CharField(max_length=100)
  Team = models.CharField(max_length=100)
  point = models.TextField(max_length=250)
  rank = models.IntegerField()
