from django.db import models
from django.conf import settings



class Genre(models.Model):
    genre_id = models.CharField(max_length=15)
    name = models.CharField(max_length=10)

    
class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=30)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    overview = models.TextField()
    release_date = models.CharField(max_length=30)
    popularity = models.FloatField()
    vote_average = models.FloatField()
    poster_path = models.CharField(max_length=100)
    trailer_url = models.CharField(max_length=100)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies")


class Rating(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField()


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


