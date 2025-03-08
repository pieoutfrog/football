from django.db import models
from django.db.models import CASCADE
from django.utils import timezone
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )


class Tournament(models.Model):
    name = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()


class Team(models.Model):
    objects = models.Manager()
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='teams', **NULLABLE)
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='logos/', **NULLABLE)
    total_games = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    goals_scored = models.IntegerField(default=0)
    goals_conceded = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def calculate_points(self):
        self.points = self.wins * 3 + self.draws
        self.save()



class Match(models.Model):
    objects = models.Manager()
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='matches', **NULLABLE)
    team1 = models.ForeignKey(Team, related_name='matches_as_team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='matches_as_team2', on_delete=models.CASCADE)
    date = models.DateField()
    score_team1 = models.IntegerField(default=0)
    score_team2 = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.team1.name} vs {self.team2.name} on {self.date}'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.score_team1 > self.score_team2:
            self.team1.wins += 1
            self.team2.losses += 1
        elif self.score_team1 < self.score_team2:
            self.team2.wins += 1
            self.team1.losses += 1
        else:
            self.team1.draws += 1
            self.team2.draws += 1
        self.team1.total_games += 1
        self.team2.total_games += 1
        self.team_1.goals_scored += self.score_team1
        self.team1.goals_conceded += self.score_team2
        self.team2.goals_scored += self.score_team2
        self.team2.goals_conceded += self.score_team1

        self.team1.calculate_points()
        self.team2.calculate_points()



class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title
