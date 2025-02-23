from django.db import models
from django.utils import timezone
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )


class Team(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='logos/', **NULLABLE)

    def __str__(self):
        return self.name


class Match(models.Model):
    objects = models.Manager()
    team1 = models.ForeignKey(Team, related_name='matches_as_team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='matches_as_team2', on_delete=models.CASCADE)
    date = models.DateField()
    score_team1 = models.IntegerField(default=0)
    score_team2 = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.team1.name} vs {self.team2.name} on {self.date}'


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
