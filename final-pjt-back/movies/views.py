from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse
from django.db.models import Q
from .serializers import SearchMovieSerializer


# Create your views here.
def get_movieList_popular(request, language, page, region):
    return


def get_movieList_toprated(request, language, page, region):
    return


def get_movieList_nowplaying(request, language, page, region):
    return


def get_movie_latest(request, language):
    return


def search_count_movie(request): #filter_list): # POST 요청 => count
    filter_list = [['title', '블랙 팬서'], ['genre_ids',[12, 18]]]
    q = Q()
    for filt in filter_list:
        field_name = filt[0]
        if field_name == 'title':
            q.add(Q(title__contains=val), q.AND)
        elif field_name == 'genre_ids':
            q.add(Q(genre_ids=val), q.AND)
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
