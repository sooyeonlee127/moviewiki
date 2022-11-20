from rest_framework import serializers
from .models import Movie, Comment


class SearchMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        
