from django.core.management.base import BaseCommand
from django.db import transaction
from ipl_app.models import Deliveries
import csv


class Command(BaseCommand):
    help = 'Command to load CSV file'

    def add_argument(self, parser):
        parser.add_argument('--pythonpath', type=str, help="file path")

    
    def handle(self, *args, **options):
        file_path = options['pythonpath']
        deliveries_reader = csv.DictReader(open(file_path))
        with transactions.atomic():
            for delivery in deliveries_reader:
                deliveries_queries = Deliveries.objects.create(
                    match_id_id=int(delivery['match_id']),
                    inning=int(delivery['inning']),
                    batting_team=str(delivery['batting_team']),
                    bowling_team=str(delivery['bowling_team']),
                    over=int(delivery['over']),
                    ball=int(delivery['ball']),
                    batsman=str(delivery['batsman']),
                    non_striker=str(delivery['non_striker']),
                    bowler=str(delivery['bowler']),
                    is_super_over=int(delivery['is_super_over']),
                    wide_runs=int(delivery['wide_runs']),
                    bye_runs=int(delivery['bye_runs']),
                    legbye_runs=int(delivery['legbye_runs']),
                    noball_runs=int(delivery['noball_runs']),
                    penalty_runs=int(delivery['penalty_runs']),
                    batsman_runs=int(delivery['penalty_runs']),
                    extra_runs=int(delivery['extra_runs']),
                    total_runs=int(delivery['total_runs']),
                    player_dismissed=str(delivery['player_dismissed']),
                    dismissal_kind=str(delivery['dismissal_kind']),
                    fielder=str(delivery['fielder'])
                )

        deliveries_queries.save()
