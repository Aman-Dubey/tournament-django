from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *


# Create your views here.
def indexViews(request):
   return HttpResponse(''' 
    <ul>
    <li><a href="/tournament">Tournament</a></li>
  <li><a href="/teams">Teams</a></li>
  <li><a href="/players">Players</a></li>
  <li><a href="/match">Matches</a></li>
</ul> 
   ''')
def playerViews(request):
    if request.method == 'GET':
        data = Players.objects.all()
        serializer = PlayersSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
def matchViews(request):
    if request.method == 'GET':
        data = Match.objects.all()
        serializer = MatchSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
def tournamentViews(request):
    if request.method == 'GET':
        data = Tournament.objects.all()
        serializer = TournamentSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
def teamViews(request):
    if request.method == 'GET':
        data = Teams.objects.all()
        serializer = TeamSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)