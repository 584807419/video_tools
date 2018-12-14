from django.urls import path, re_path
from film_search.views import FilmSearch
app_name = "courses"
urlpatterns = [
    path('film_search_result/', FilmSearch.as_view(), name="film_search_result"),
]
