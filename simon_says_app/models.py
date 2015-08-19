import random

from django.db import models
from django.conf import settings

# Create your models here.

class Game(models.Model):
    sequence = models.CharField(max_length=100, default='')
    # don't populate score until game is over
    score = models.IntegerField(default=0)
    player = models.ForeignKey(settings.AUTH_USER_MODEL)

    def is_finished(self):
        return self.score is not 0


def generate_pattern():
    return ''.join(random.choice('RYGB') for _ in range(100))
