from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User
# Create your models here.



class Player(models.Model):
  first_name=models.CharField(max_length=50,null=True)
  last_name=models.CharField(max_length=50, null=True)
  nba_team=models.CharField(max_length=50, null=True)
  nba_team=models.CharField(max_length=50, null=True)
  point_rating=models.IntegerField(null=True)
  rebound_rating=models.IntegerField(null=True)
  assist_rating=models.IntegerField(null=True)
  steal_rating=models.IntegerField(null=True)
  block_rating=models.IntegerField(null=True)
  turnover_rating=models.IntegerField(null=True)
  threepointer_rating=models.IntegerField(null=True)
  status=models.BooleanField(null=True) #True means player available / False Player is taken
  
class Team(models.Model):
  roster = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
  team_name=models.CharField(max_length=50,null=True)
  team_points=models.IntegerField(null=True)
  team_rebounds=models.IntegerField(null=True)
  team_assists=models.IntegerField(null=True)
  team_steals=models.IntegerField(null=True)
  team_blocks=models.IntegerField(null=True)
  team_turnovers=models.IntegerField(null=True)
  team_threepointers=models.IntegerField(null=True)

class Profile(models.Model):
  user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  user_name=models.CharField(max_length=100, null=True)
  team=models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
  points=models.TextField(max_length=250, null=True)
  rank=models.IntegerField(null=True)
  wins=models.IntegerField(null=True)
  losses=models.IntegerField(null=True)

  def get_absolute_url(self):
    return reverse('team_detail', kwargs={'team_id':self.id})

  