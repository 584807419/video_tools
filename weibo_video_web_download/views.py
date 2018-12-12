import re
import time
from urllib.parse import unquote
from selenium import webdriver
from django.shortcuts import render

# Create your views here.
from django.views import View


class IndexView(View):
    @staticmethod
    def get(request):
        return render(request, 'weibo/base.html', {})


class AnalyzeUrl(View):
    """https://weibo.com/tv/v/H6QyX4qVM?fid=1034:4316319986740109"""
    @staticmethod
    def post(request):
        real_video_url = None
        url = request.POST.get("weibo_video_url", "")
        if not url:
            return render(request, 'weibo/base.html', {"error": "不给我地址让我分析个啥?"})
        # mac上
        driver = webdriver.PhantomJS(executable_path='/Users/zhangkun/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
        # 服务器上
        # driver = webdriver.PhantomJS(executable_path='/home/zk/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
        driver.get(url)
        time.sleep(3)
        pattern = re.compile(r'video_src=(.+?)video&amp;', re.DOTALL)  # 查找数字
        find_video_src = pattern.findall(driver.page_source)
        if find_video_src:
            real_video_url = find_video_src[0]
        if real_video_url:
            real_url = "http:" + unquote(real_video_url) + "video"
            return render(request, 'weibo/base.html', {"real_url": real_url})
        if not real_video_url:
            return render(request, 'weibo/base.html', {"error": "解析失败,请重新复制链接重试,还不行,请联系张昆帮你"})
