from django.urls import path,include
from .views import *
urlpatterns = [
    path('',indexViews,name='index'),
    path('match/',matchViews,name='match'),
    path('players/',playerViews,name='player'),
    path('tournament/',tournamentViews,name='tournament'),
    path('teams/',teamViews,name='team'),
]
