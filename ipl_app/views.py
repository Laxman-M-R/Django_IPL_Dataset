from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from django.db.models import Count, Sum, Case, Q, F, FloatField, ExpressionWrapper, Case, When
from django.http import HttpResponse, JsonResponse
from django.db import models
import json
from .models import Matches, Deliveries


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@cache_page(CACHE_TTL)
def index(request):
    return render(request, 'ipl_app/index.html')


@cache_page(CACHE_TTL)
def matches_played(request):
    matches_played = list(Matches.objects.values(
        'season').annotate(matches_played=Count('season')).order_by('season'))
    return JsonResponse(matches_played, safe=False)

@cache_page(CACHE_TTL)
def matches_played_chart(request):
    matches_played = Matches.objects.values(
        'season').annotate(matches_played=Count('season')).order_by('season')
    context = {
        'matches_played': matches_played,
    }
    return render(request, 'ipl_app/matches_played.html', context)
    
    

@cache_page(CACHE_TTL)
def matches_won(request):
    matches_won = list(Matches.objects.values(
        'season', 'winner').annotate(matches_won=Count('winner')))    
    return JsonResponse(matches_won, safe=False)

@cache_page(CACHE_TTL)
def matches_won_chart(request):
    matches_won = list(Matches.objects.values(
        'season', 'winner').annotate(matches_won=Count('winner')))
    context = {
        'matches_won': json.dumps(matches_won),
    }
    return render(request, 'ipl_app/matches_won.html', context)




@cache_page(CACHE_TTL)
def extra_runs(request):
    extra_runs = list(Deliveries.objects.filter(match_id__season=2016).values(
        'bowling_team').annotate(extra_runs=Sum('extra_runs')))    
    return JsonResponse(extra_runs, safe=False)

@cache_page(CACHE_TTL)
def extra_runs_chart(request):
    extra_runs = Deliveries.objects.filter(match_id__season=2016).values(
        'bowling_team').annotate(extra_runs=Sum('extra_runs'))
    context = {
        'extra_runs': extra_runs,
    }
    return render(request, 'ipl_app/extra_runs.html', context)




@cache_page(CACHE_TTL)
def econ_bowlers(request):    
    econ_bowlers = list(Deliveries.objects.filter(match_id__season=2015).values('bowler').annotate(total_runs=Sum('total_runs')).annotate(balls=Count('bowler', filter=Q(noball_runs=0)&Q(wide_runs=0))).annotate(economy=ExpressionWrapper(F('total_runs')/(F('balls')/6),output_field=FloatField())).order_by('economy'))[:10]  
    return JsonResponse(econ_bowlers, safe=False)

@cache_page(CACHE_TTL)
def econ_bowlers_chart(request):    
    econ_bowlers = Deliveries.objects.filter(match_id__season=2015).values('bowler').annotate(total_runs=Sum('total_runs')).annotate(balls=Count('bowler', filter=Q(noball_runs=0)&Q(wide_runs=0))).annotate(economy=ExpressionWrapper(F('total_runs')/(F('balls')/6),output_field=FloatField())).order_by('economy')[:10]
    context = {
        'econ_bowlers': econ_bowlers,
    }
    return render(request, 'ipl_app/econ_bowlers.html', context)


@cache_page(CACHE_TTL)
def stories(request):      
    twwbr = Matches.objects.filter(~Q(win_by_runs=0), toss_winner=F('winner')).count()
    twwbw = Matches.objects.filter(~Q(win_by_wickets=0), toss_winner=F('winner')).count()
    tlwbr = Matches.objects.filter(~Q(win_by_runs=0), ~Q(toss_winner=F('winner'))).count()
    tlwbw = Matches.objects.filter(~Q(win_by_wickets=0), ~Q(toss_winner=F('winner'))).count()  
    wins = {
        'Toss Winner Win By Runs': twwbr,
        'Toss Winner Win By Wickets': twwbw,
        'Toss Loser Win By Runs': tlwbr,
        'Toss Loser Win By Wickets': tlwbw
    }      
    return JsonResponse(list(wins.items()), safe=False)

@cache_page(CACHE_TTL)
def stories_chart(request):     
    context = {}
    context['twwbr'] = Matches.objects.filter(~Q(win_by_runs=0), toss_winner=F('winner')).count()
    context['twwbw'] = Matches.objects.filter(~Q(win_by_wickets=0), toss_winner=F('winner')).count()
    context['tlwbr'] = Matches.objects.filter(~Q(win_by_runs=0), ~Q(toss_winner=F('winner'))).count()
    context['tlwbw'] = Matches.objects.filter(~Q(win_by_wickets=0), ~Q(toss_winner=F('winner'))).count()
    return render(request, 'ipl_app/stories.html', context)
