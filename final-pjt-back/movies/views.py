from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import SearchMovieSerializer, CommentSerializer
from .models import Movie


# Create your views here.
@api_view(['GET', 'POST'])
def get_movieList_popular(request): # main 페이지
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = SearchMovieSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_movieList_popular_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'GET':
        serializer = SearchMovieSerializer(movie)
        return Response(serializer.data)




def get_movieList_toprated(request, language, page, region):
    return


def get_movieList_nowplaying(request, language, page, region):
    return


def get_movie_latest(request, language):
    return


def search_count_movie(request): #filter_list): # POST 요청 => count
    filter_list = [['title', '블랙 팬서', False], ['title', '아바타', False]]
    q = Q()
    for filt in filter_list:
        field_name, val, isContain = filt
        if field_name == 'title':
            if isContain:
                q.add(Q(title__contains=val), q.AND)
            else:
                q.add(~Q(title__contains=val), q.AND)
        elif field_name == 'adult':
            if isContain:
                q.add(Q(adult=val), q.AND)
            else:
                q.add(~Q(adult=val), q.AND)
        elif field_name == 'genre_ids':
            if isContain:
                q.add(Q(genre_ids=val), q.AND)
            else:
                q.add(~Q(genre_ids=val), q.AND)
    result = Movie.objects.filter(q)
    serializer = SearchMovieSerializer(result, many=True)
    
    return JsonResponse(serializer.data, safe=False)

# filter_list = [
#     ['title', '와칸다'],
#     ['genres_ids', '로맨스'],
# ]


    '''
    search_type : Integer
    1: 장르 => integer(genre_id)
    2: 연령(true false) => boolean
    3: 평점순 정렬 => boolean(True)
    4: 키워드 => list(id, name)

    search_value : Integer or Boolean or list

    '''




# review 관련 view
@api_view(['POST'])
def comment_create(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

