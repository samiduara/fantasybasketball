from django.contrib import admin

from .models import Profile, Team, Player

admin.site.register(Profile)
admin.site.register(Team)
admin.site.register(Player)