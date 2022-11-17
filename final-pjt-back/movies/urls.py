from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('popular/', views.get_movieList_popular, name="popular"),
    path('search/', views.get_movie_latest, name="search"),
]



'''
path('search/', views.get_movieList_latest, name="latest")


def search_movie(request, search_type, search_value, filter_list):
    return filter_list

search_type : Integer
1: 장르 => integer(genre_id)
2: 연령(true false) => boolean
3: 평점순 정렬 => boolean(True)
4: 키워드 => list(id, name)

search_value : Integer or Boolean or list




filter_list => [1000, ]
filter_list => [512, 장르()]
filter_list => [153, 장르(), 장르(),]
filter_list => [67, 장르(), 장르(), 연령, ]
filter_list => [12, 장르(), 장르(), 연령, 키워드, ]
filter_list => [6, 장르(), 장르(), 연령, 키워드, 키워드, ]


'''