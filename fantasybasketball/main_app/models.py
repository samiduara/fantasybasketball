from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Player(models.Model):
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  user_name = models.CharField(max_length=100)
  team = models.CharField(max_length=100)
  points = models.TextField(max_length=250)
  rank = models.IntegerField()
