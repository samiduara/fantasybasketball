from django.db import models

# Create your models here.
class Player(models.Model):
  api_id=models.IntegerField()
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)