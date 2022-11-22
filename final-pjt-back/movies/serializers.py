from rest_framework import serializers
from .models import Movie, Comment


class SearchMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie',)



class MovieSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
