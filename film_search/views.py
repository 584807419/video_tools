import re
import time
import requests
from urllib.parse import unquote,quote
from bs4 import BeautifulSoup

from django.shortcuts import render
from video_tools.settings import driver
# Create your views here.
from django.views import View



class FilmSearch(View):
    @staticmethod
    def post(request):
        web_url = "https://www.ysshare.com"
        search_url = "https://www.ysshare.com/search/"
        film_name = request.POST.get("film_name", "")
        url = search_url+quote(film_name)
        web_res = requests.get(url)
        web_page = web_res.content
        if web_res.status_code != 200:
            driver.get(url)
            web_page = driver.page_source
        soup = BeautifulSoup(web_page)
        res = []
        for i in soup.select("div.panel-body div.title-wrapper h3"):
            film_detail_url = web_url+i.contents[0].attrs.get("href")
            name = i.text
            res.append({"film_name": name, "film_url": film_detail_url})
        return render(request, 'film/base.html', {"film_search_res": res})
