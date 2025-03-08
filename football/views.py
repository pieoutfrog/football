from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post, Team, Match

def post_list(request):
    posts = Post.published.all()
    return render(
        request,
        'football/post/list.html',
        {'posts': posts}
    )



def team_list(request):
    teams = Team.objects.all()
    return render(
        request,
        'football/team/list.html',
        {'teams': teams}
    )


def match_list(request):
    matches = Match.objects.all()
    return render(
        request,
        'football/match/list.html',
        {'matches': matches}
    )



def post_detail(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )
    return render(
        request,
        'football/post/detail.html',
        {'post': post}
    )


def team_detail(request, id):
    team = get_object_or_404(
        Team,
        id=id
    )
    return render(
        request,
        'football/team/detail.html',
        {'team': team}
    )


def match_detail(request, id):
    match = get_object_or_404(
        Match,
        id=id
    )
    return render(
        request,
        'football/match/detail.html',
        {'match': match}
    )