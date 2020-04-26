from django.db import models

# Create your models here.
class Teams(models.Model):
    name=models.CharField(max_length=100)
    owner=models.CharField(max_length=100)
    logo=models.ImageField(upload_to='media',blank=True)
class Players(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=25)
    nationality=models.CharField(max_length=30, default='INDIA')
    team=models.ForeignKey(Teams, on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='media',blank=True)
class Tournament(models.Model):
    name=models.CharField(max_length=100, blank=True, default='')
    started_on=models.DateTimeField()
    no_of_teams=models.IntegerField(default=10)
    no_of_matches=models.IntegerField(default=45)
    man_of_series=models.OneToOneField(Players,on_delete=models.CASCADE)
class Match(models.Model):
    match_date=models.DateTimeField()
    location=models.CharField(max_length=50)
    man_of_match=models.ForeignKey(Players,on_delete=models.CASCADE)
    teams=models.ForeignKey(Teams,on_delete=models.CASCADE)
