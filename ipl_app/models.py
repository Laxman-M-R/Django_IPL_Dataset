from django.db import models

# Create your models here.
from django.db import models

class Matches(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    season = models.IntegerField(default = 0)
    city = models.CharField(max_length = 200)
    date_played = models.DateField()
    team1 = models.CharField(max_length = 200) 
    team2 = models.CharField(max_length = 200) 
    toss_winner = models.CharField(max_length = 200)
    toss_decision = models.CharField(max_length = 100)
    result = models.CharField(max_length = 100)
    dl_applied = models.IntegerField(default = 0)
    winner = models.CharField(max_length = 200)
    win_by_runs = models.IntegerField(default = 0)
    win_by_wickets = models.IntegerField(default = 0)
    player_of_match = models.CharField(max_length = 200)
    venue = models.CharField(max_length = 200)
    umpire1 = models.CharField(max_length = 200)
    umpire2 = models.CharField(max_length = 200)
    umpire3 = models.CharField(max_length = 200)

     
    class Meta:
        db_table = 'matches' 
    
    
class Deliveries(models.Model):
    match_id = models.ForeignKey(Matches, on_delete = models.CASCADE)
    inning = models.IntegerField(default = 0)
    batting_team = models.CharField(max_length = 200)
    bowling_team = models.CharField(max_length = 200)
    over = models.IntegerField(default = 0)
    ball = models.IntegerField(default = 0)
    batsman = models.CharField(max_length = 200)
    non_striker = models.CharField(max_length = 200)
    bowler = models.CharField(max_length = 200)
    is_super_over = models.IntegerField(default = 0)
    wide_runs = models.IntegerField(default = 0)
    bye_runs = models.IntegerField(default = 0)
    legbye_runs = models.IntegerField(default = 0)
    noball_runs = models.IntegerField(default = 0)
    penalty_runs = models.IntegerField(default = 0)
    batsman_runs = models.IntegerField(default = 0)
    extra_runs = models.IntegerField(default = 0)
    total_runs = models.IntegerField(default = 0)
    player_dismissed = models.CharField(max_length = 200)
    dismissal_kind = models.CharField(max_length = 100)
    fielder = models.CharField(max_length = 100)

    class Meta:
        db_table = 'deliveries'