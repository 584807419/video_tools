import re
import time
import requests
from urllib.parse import unquote, quote
from bs4 import BeautifulSoup

from django.shortcuts import render
from video_tools.settings import driver
# Create your views here.
from django.views import View


class FilmSearch(View):
    @staticmethod
    def post(request):
        # web_url = "https://www.ysshare.com"
        # search_url = "https://www.ysshare.com/search/"
        # film_name = request.POST.get("film_name", "")
        # url = search_url+quote(film_name)
        # web_res = requests.get(url)
        # web_page = web_res.content
        # if web_res.status_code != 200:
        #     driver.get(url)
        #     web_page = driver.page_source
        # soup = BeautifulSoup(web_page)
        # res = []
        # for i in soup.select("div.panel-body div.title-wrapper h3"):
        #     film_detail_url = web_url+i.contents[0].attrs.get("href")
        #     name = i.text
        #     res.append({"film_name": name, "film_url": film_detail_url})
        #
        # return render(request, 'film/base.html', {"film_search_res": res})

        web_url = "https://www.ysshare.com"
        search_url = "https://www.ysshare.com/search/"
        film_name = request.POST.get("film_name", "")
        url = search_url + quote(film_name)
        web_res = requests.get(url)
        web_page = web_res.content
        if web_res.status_code != 200:
            driver.get(url)
            web_page = driver.page_source
        soup = BeautifulSoup(web_page)
        res = []
        for i in soup.select("div.panel-body div.search-content div.row"):
            all_text = i.text

            try:
                film_name = i.contents[0].contents[0].contents[0].attrs.get("title")
            except:
                film_name = ""

            try:
                film_year = all_text.split("简介")[0].split("导演:")[0].split("(")[1].split(")")[0]
            except:
                film_year = ""

            try:
                film_type = all_text.split("简介")[0].split("导演:")[0].split("(")[1].split(")")[1]
            except:
                film_type = ""

            try:
                film_director = all_text.split("简介")[0].split("导演:")[1].split("演员")[0]
            except:
                film_director = ""

            try:
                film_actor = all_text.split("简介")[0].split("导演:")[1].split("演员:")[1].split("类型")[0]
            except:
                film_actor = ""

            try:
                film_area = all_text.split("简介")[0].split("导演:")[1].split("演员:")[1].split("类型:")[1].split("地区:")[1]
            except:
                film_area = ""

            try:
                film_desc = all_text.split("简介")[1]
            except:
                film_desc = ""

            try:
                film_image_url = i.contents[0].contents[0].contents[0].contents[0].attrs.get("src")
            except:
                film_image_url = ""

            try:
                film_page_url = web_url + i.contents[0].contents[0].contents[0].attrs.get("href")
            except:
                film_page_url = ""

            try:
                film_style = all_text.split("简介")[0].split("导演:")[1].split("演员:")[1].split("类型:")[1].split("地区")[0]
            except:
                film_style = ""

            film_dict = {"all_text": all_text,
                         "film_name": film_name,
                         "film_year": film_year,
                         "film_type": film_type,
                         "film_director": film_director,
                         "film_actor": film_actor,
                         "film_style": film_style,
                         "film_area": film_area,
                         "film_desc": film_desc,

                         "film_image_url": film_image_url,
                         "film_page_url": film_page_url,
                         }
            res.append(film_dict)

        return render(request, 'film/base.html', {"film_search_res": res})