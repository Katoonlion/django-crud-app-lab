from django.db import models
from django.urls import reverse

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    rating = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('game-detail', kwargs={'game_id': self.id})