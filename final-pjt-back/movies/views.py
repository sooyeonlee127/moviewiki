from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import get_object_or_404, get_list_or_404
# from django.views.decorators.http import require_POST
from .serializers import SearchMovieSerializer, CommentSerializer, MovieSerializer
from .models import Movie, Comment
import json # json 파일 파싱용


# Create your views here.
@api_view(['GET', 'POST'])
def get_movieList_popular(request): # main 페이지
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = SearchMovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data, safe=False)




def filter_movie(filter_list):
     # print(filter_list)
    q = Q()
    for item in filter_list:
        print(item)
        isContain = int(item['answers_option'])
        if isContain == 2: continue # 0:소거, 1:포함, 2:스킵
        for val in item['field_value']:
            if item['field_name'] == 'title':
                if isContain:
                    q.add(Q(title__contains=val), q.AND)
                else:
                    q.add(~Q(title__contains=val), q.AND)
            elif item['field_name'] == 'adult':
                if isContain:
                    q.add(Q(adult=val), q.AND)
                else:
                    q.add(~Q(adult=val), q.AND)
            elif item['field_name'] == 'genre_ids':
                if isContain:
                    q.add(Q(genre_ids=val), q.AND)
                else:
                    q.add(~Q(genre_ids=val), q.AND)
            elif item['field_name'] == 'release_date':
                if isContain:
                    q.add(Q(release_date__startswith=val), q.AND)
                else:
                    q.add(~Q(release_date__startswith=val), q.AND)
            elif item['field_name'] == 'original_language':
                if isContain:
                    q.add(Q(original_language=val), q.AND)
                else:
                    q.add(~Q(original_language=val), q.AND)
            elif item['field_name'] == 'popularity':
                if isContain:
                    q.add(Q(popularity__gt=val), q.AND)
                else:
                    q.add(~Q(popularity__gt=val), q.AND)

    return Movie.objects.filter(q)
    

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def search_movie_get_count(request): # request(POST) : filter_list => return : count
    
    filter_list = json.loads(request.body)['filter_list']
    print('------------------')
    print('get_count')
    print(filter_list)
    result = {
        'count' : len(filter_movie(filter_list)),
    }
    return JsonResponse(json.dumps(result), safe=False)


@api_view(['POST'])
def search_movie_get_result(request):
    filter_list = json.loads(request.body)['filter_list']
    print('result')
    print(filter_list)
    result = filter_movie(filter_list)
    serializer = SearchMovieSerializer(result, many=True)
    return JsonResponse(serializer.data, safe=False)


# review 관련 view
@api_view(['POST'])
def comment_create(request, movie_id):
    rating = request.data['rating']
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user, rating=rating)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)




@api_view(['POST'])
def create_movie(request):
    serializer = SearchMovieSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
