from django.db import models
from django.conf import settings



class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)

    
class Movie(models.Model):
    adult = models.BooleanField()
    backdrop_path = models.CharField(max_length=100)
    genre_ids = models.ManyToManyField(Genre, related_name='movie_ids')
    id = models.IntegerField(primary_key=True)
    original_language = models.CharField(max_length=10)
    original_title = models.CharField(max_length=50)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=100)
    release_date = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    video = models.BooleanField(max_length=100)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()

    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies")


# class Rating(models.Model):
#     movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     score = models.IntegerField()


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


