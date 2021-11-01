from django.db import models
from django.db.models.deletion import CASCADE

class Event(models.Model):

    game = models.ForeignKey("Game", on_delete=CASCADE)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    organizer = models.ForeignKey("Gamer", on_delete=CASCADE)
    