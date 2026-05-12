from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Game(models.Model):
    title = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    rating = models.IntegerField()
    description = models.TextField(max_length=250)
    tags = models.ManyToManyField(Tag, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('game-detail', kwargs={'game_id': self.id})
    


class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    player_name = models.CharField(max_length=100)
    comment = models.TextField(max_length=250)
    rating = models.IntegerField()

    def __str__(self):
        return self.comment