from django.urls import path
from . import views


app_name = 'football'

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),

    path('matches/list/', views.match_list, name='match_list'),
    path('matches/<int:id>/', views.match_detail, name='match_detail'),

    path('teams/list/', views.team_list, name='team_list'),
    path('teams/<int:id>/', views.team_detail, name='team_details')
]