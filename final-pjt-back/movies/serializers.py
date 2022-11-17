from rest_framework import serializers
from .models import Movie


class SearchMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

# movie_id, user_id 가져와야 함.
# class CommentSerializer(serializers.ModelSerializer):
#     user_id = serializers.IntegerField(source='user.id', read_only=True)
#     movie_set = SearchMovieSerializer(many=True, read_only=True)

#     class Meta:
#         model = Comment
#         fields = '__all__'
#         read_only_fields = ('user', )
