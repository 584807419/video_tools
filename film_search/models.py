from django.db import models

# Create your models here.

class FilmData(models.Model):
    film_name = models.CharField(default="", blank=True, null=True, max_length=50)
    film_director = models.CharField(default="", blank=True, null=True, max_length=50)
    film_actor = models.CharField(default="", blank=True, null=True, max_length=50)
    film_type = models.CharField(default="", blank=True, null=True, max_length=50)
    film_area = models.CharField(default="", blank=True, null=True, max_length=50)
    film_desc =  models.CharField(default="", blank=True, null=True, max_length=255)
    film_image_url = models.CharField(default="", blank=True, null=True, max_length=255)
    film_page_url = models.CharField(default="", blank=True, null=True, max_length=255)
    film_download_info = models.TextField(default="", blank=True, null=True)