from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('matches_played/', views.matches_played, name="matches_played"),
    path('matches_won/', views.matches_won, name="matches_won"),
    path('extra_runs/', views.extra_runs, name="extra_runs"),
    path('econ_bowlers/', views.econ_bowlers, name="econ_bowlers"),
    path('stories/', views.stories, name="stories"),
    path('matches_played_chart/', views.matches_played_chart, name="matches_played_chart"),
    path('matches_won_chart/', views.matches_won_chart, name="matches_won_chart"),
    path('extra_runs_chart/', views.extra_runs_chart, name="extra_runs_chart"),
    path('econ_bowlers_chart/', views.econ_bowlers_chart, name="econ_bowlers_chart"),
    path('stories_chart/', views.stories_chart, name="stories_chart"),    
]