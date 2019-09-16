from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Team(models.Model):
  roster = models.ForeignKey(Player)
  team_name=models.CharField(max_length=50)
  team_points=models.IntegerField()
  team_rebounds=models.IntegerField()
  team_assists=models.IntegerField()
  team_steals=models.IntegerField()
  team_blocks=models.IntegerField()
  team_turnovers=models.IntegerField()
  team_threepointers=models.IntegerField()


class Player(models.Model):
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  nba_team=models.CharField(max_length=50)
  point_rating=models.IntegerField()
  rebound_rating=models.IntegerField()
  assist_rating=models.IntegerField()
  steal_rating=models.IntegerField()
  block_rating=models.IntegerField()
  turnover_rating=models.IntegerField()
  threepointer_rating=models.IntegerField()
  status=models.BooleanField() #True means player available / False Player is taken
  

class Profile(models.Model):
  user=models.OneToOneField(User, on_delete=models.CASCADE)
  user_name=models.CharField(max_length=100)
  team=models.ForeignKey(Team)
  points=models.TextField(max_length=250)
  rank=models.IntegerField()
  wins=models.IntegerField()
  losses=models.IntegerField()
