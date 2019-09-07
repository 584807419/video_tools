import re
import sys
import time
from urllib.parse import unquote

from django.shortcuts import render
from selenium import webdriver
# Create your views here.
from django.views import View
from django.utils.decorators import method_decorator
from common_utils.log_tools.log_decorator import func_var_record
from videoedit.models import VideoEditSoftware


# 怎么调用日志工具
# @func_var_record
# def functest(request):
#     ddd = 323232
#     ddd3 = 323232
#     return ddd,ddd3,locals()
#
# @func_var_record
# def functest1(**kwargs):
#     ddd = 3232324444
#     return ddd, locals()
#
# class IndexView(View):
#     @method_decorator(func_var_record)
#     def get(self, request):
#         a = 3
#         b = 3
#         dasd = functest(request)
#         dasd1 = functest1(request=request)
#         return render(request, 'weibo/index.html', {}), locals()

class IndexView(View):
    def get(self, request):
        return render(request, 'weibo/index.html',
                      {'videoedit_software_info': VideoEditSoftware.objects.all().order_by('name')})


class AnalyzeUrl(View):
    """https://weibo.com/tv/v/H6QyX4qVM?fid=1034:4316319986740109"""

    @staticmethod
    def post(request):
        if sys.platform == "darwin":  # mac上
            driver = webdriver.PhantomJS(
                executable_path='/Users/zhangkun/Documents/GitHub/video_tools/phantomjs-2.1.1-macosx/bin/phantomjs')
        if sys.platform == "win32":  # windows上
            driver = None
        if "linux" in sys.platform:  # ubuntu上
            driver = webdriver.PhantomJS(executable_path='/home/zk/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
        real_video_url = None
        url = request.POST.get("weibo_video_url", "")
        if "weibo.com/tv/v/" not in url:
            return render(request, 'weibo/index.html', {"error": "检查复制过来的网址重试下吧！"})
        driver.get(url)
        pattern = re.compile(r'video_src=(.+?)video&amp;', re.DOTALL)  # 查找数字
        _num_temp = 0
        while "video_src=" not in driver.page_source:
            time.sleep(0.5)
            _num_temp += 1
            if _num_temp > 20:
                return render(request, 'weibo/index.html', {"error": "解析失败,超时,请重新复制链接重试,还不行,请联系张昆帮你"})
        find_video_src = pattern.findall(driver.page_source)

        driver.quit()
        
        if find_video_src:
            real_video_url = find_video_src[0]
        if real_video_url:
            real_url = "http:" + unquote(real_video_url) + "video"
            return render(request, 'weibo/index.html', {"real_url": real_url})
        if not real_video_url:
            return render(request, 'weibo/index.html', {"error": "解析失败,请重新复制链接重试,还不行,请联系张昆帮你"})
