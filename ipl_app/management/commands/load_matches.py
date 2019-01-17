from django.core.management.base import BaseCommand
from django.db import transaction
from ipl_app.models import Matches
import csv


class Command(BaseCommand):
    help = 'Command to load CSV file'

    def add_argument(self, parser):
        parser.add_argument('--pythonpath', type=str, help="file path")

    
    def handle(self, *args, **options):
        file_path = options['pythonpath']
        matches_reader = csv.DictReader(open(file_path))
        with transactions.atomic():
            for match in matches_reader:
                matches_queries = Matches.objects.create(
                    id=int(match['id']),
                    season=int(match['season']),
                    city=str(match['city']),
                    date_played=(match['date']),
                    team1=str(match['team1']),
                    team2=str(match['team2']),
                    toss_winner=str(match['toss_winner']),
                    toss_decision=str(match['toss_decision']),
                    result=str(match['toss_decision']),
                    dl_applied=int(match['dl_applied']),
                    winner=str(match['winner']),
                    win_by_runs=int(match['win_by_runs']),
                    win_by_wickets=int(match['win_by_wickets']),
                    player_of_match=str(match['player_of_match']),
                    venue=str(match['venue']),
                    umpire1=str(match['umpire1']),
                    umpire2=str(match['umpire2']),
                    umpire3=str(match['umpire3'])
                )

        matches_queries.save()
