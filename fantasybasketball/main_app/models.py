from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  user_name = models.CharField(max_length=100)
  Team = models.CharField(max_length=100)
  point = models.TextField(max_length=250)
  rank = models.IntegerField()
