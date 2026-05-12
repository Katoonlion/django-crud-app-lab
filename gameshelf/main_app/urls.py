from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.game_index, name='game-index'),
    path('games/<int:game_id>/', views.game_detail, name='game-detail'),

    path('games/create/', views.GameCreate.as_view(), name='game-create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='game-update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='game-delete'),

    path('games/<int:game_id>/add_review/', views.add_review, name='add-review'),
    path('reviews/<int:pk>/update/', views.ReviewUpdate.as_view(), name='review-update'),
    path('reviews/<int:pk>/delete/', views.ReviewDelete.as_view(), name='review-delete'),

    path('tags/', views.tag_index, name='tag-index'),
    path('tags/create/', views.TagCreate.as_view(), name='tag-create'),
    path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tag-delete'),

    path('accounts/signup/', views.signup, name='signup'),
]