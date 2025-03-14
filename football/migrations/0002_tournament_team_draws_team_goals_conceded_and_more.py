# Generated by Django 5.0.12 on 2025-02-24 05:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='draws',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='goals_conceded',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='goals_scored',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='losses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='total_games',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='wins',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='football.tournament'),
        ),
        migrations.AddField(
            model_name='team',
            name='tournament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='football.tournament'),
        ),
    ]
