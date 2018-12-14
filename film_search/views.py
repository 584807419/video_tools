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

                         "film_image_url": film_image_url.replace("https","http"),
                         "film_page_url": film_page_url,
                         }
            res.append(film_dict)

        return render(request, 'film/base.html', {"film_search_res": res})


class FilmDownload(View):
    def post(self,request):
        film_name = request.POST.get("film_name")
        web_res= requests.get(request.POST.get("film_page_url"))
        web_page = web_res.content
        _temp_dict = {"baidu":[],
                      "ed2k":[],
                      "magnet":[],
                      "ftp":[]
                      }
        for i in BeautifulSoup(web_page).find_all("li",class_="col-xs-12 input-group has-success thunder-deal"):
            dw_url = i.attrs.get("data-link")
            if dw_url:
                if "baidu" in dw_url:
                    _temp_dict["baidu"].append(dw_url)
                if "ed2k" in dw_url:
                    _temp_dict["ed2k"].append(dw_url.replace("www.ysshare.com","www.videotools.cn"))
                if "magnet" in dw_url:
                    _temp_dict["magnet"].append(dw_url.replace("www.ysshare.com", "www.videotools.cn"))
                if "ftp" in dw_url:
                    _temp_dict["ftp"].append(dw_url.replace("www.ysshare.com", "www.videotools.cn"))
        return render(request, 'film/dw_info.html', {"temp_dict": _temp_dict})