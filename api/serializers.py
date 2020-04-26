from rest_framework import serializers
from .models import *
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ['name', 'owner', 'logo',]
class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = ['name', 'age', 'nationality','team','profile_pic']
class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['name', 'started_on', 'no_of_teams','no_of_matches','man_of_series']
class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['match_data', 'location', 'man_of_match','teams']
