from django.shortcuts import render
from .models import Movie


# Create your views here.
def get_movieList_popular(request, language, page, region):
    return


def get_movieList_toprated(request, language, page, region):
    return


def get_movieList_nowplaying(request, language, page, region):
    return


def get_movie_latest(request, language):
    return


def search_movie(request, filter_list, search_type, search_value):
    movies = Movie.objects.all()


    '''
    search_type : Integer
    1: 장르 => integer(genre_id)
    2: 연령(true false) => boolean
    3: 평점순 정렬 => boolean(True)
    4: 키워드 => list(id, name)

    search_value : Integer or Boolean or list

    '''
    return filter_list
