# Generated by Django 3.2.9 on 2021-11-03 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_auto_20211103_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='attending_events',
        ),
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='attending_events', through='levelupapi.EventGamer', to='levelupapi.Gamer'),
        ),
    ]