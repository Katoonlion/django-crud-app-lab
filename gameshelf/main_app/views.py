from django.shortcuts import render, redirect
from .models import Game, Review, Tag
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponseForbidden


# Create your views here.

# Game
def home(request):
    return render(request, 'home.html')


def game_index(request):
    
    games = Game.objects.all()

    return render(request, 'games/index.html', {
        'games': games
    })


def game_detail(request, game_id):

    game = Game.objects.get(id=game_id)
    review_form = ReviewForm()

    return render(request, 'games/detail.html', {
        'game': game,
        'review_form': review_form
    })


class GameCreate(LoginRequiredMixin, CreateView):

    model = Game

    fields = fields = ['title', 'platform', 'genre', 'status', 'rating', 'description', 'tags']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GameUpdate(LoginRequiredMixin, UpdateView):
    model = Game
    fields = ['title', 'platform', 'genre', 'status', 'rating', 'description', 'tags']


class GameDelete(LoginRequiredMixin, DeleteView):
    model = Game
    success_url = '/games/'


# Review

@login_required
def add_review(request, game_id):

    form = ReviewForm(request.POST)

    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.game_id = game_id
        new_review.user = request.user
        new_review.save()

    return redirect('game-detail', game_id=game_id)



class ReviewUpdate(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['player_name', 'comment', 'rating']

    def get_success_url(self):
        return self.object.game.get_absolute_url()


class ReviewDelete(LoginRequiredMixin, DeleteView):
    model = Review

    def get_success_url(self):
        return self.object.game.get_absolute_url()
    


# Tag

class TagCreate(LoginRequiredMixin, CreateView):
    model = Tag
    fields = ['name']
    success_url = '/tags/'


class TagUpdate(LoginRequiredMixin, UpdateView):
    model = Tag
    fields = ['name']
    success_url = '/tags/'


class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    success_url = '/tags/'


def tag_index(request):
    tags = Tag.objects.all()

    return render(request, 'tags/index.html', {
        'tags': tags
    })


    
# Sign up

def signup(request):

    error_message = ''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('game-index')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()

    return render(request, 'registration/signup.html', {
        'form': form,
        'error_message': error_message
    })

