from django.urls import path, re_path
# from videoedit.views import IndexView,IndexView
from django.views.generic import TemplateView
#
urlpatterns = [
    path('', TemplateView.as_view(template_name="videoedit/index.html"), name="index"),
    # path('analyze_url/', AnalyzeUrl.as_view(), name="analyze_url"),
]
