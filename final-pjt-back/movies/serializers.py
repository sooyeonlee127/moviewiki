from rest_framework import serializers
from .models import Movie


class SearchMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
