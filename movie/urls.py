
from django.contrib import admin
from django.urls import path
from views import movie_review

urlpatterns = [
    path('', movie_review, 'movie_review'),
]