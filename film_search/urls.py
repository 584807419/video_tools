from django.urls import path, re_path
from film_search.views import FilmSearch, FilmDownload

#
urlpatterns = [
    path('film_search_result/', FilmSearch.as_view(), name="film_search_result"),
    path('film_download_result/', FilmDownload.as_view(), name="film_download_result"),
]
