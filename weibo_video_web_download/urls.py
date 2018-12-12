from django.urls import path, re_path
from weibo_video_web_download.views import AnalyzeUrl,IndexView
app_name = "courses"
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('analyze_url/', AnalyzeUrl.as_view(), name="analyze_url"),
]
