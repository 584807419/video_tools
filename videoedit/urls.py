from django.urls import path, re_path
from videoedit.views import AllSoftWareInfo
from django.views.generic import TemplateView
#
urlpatterns = [
    path('', TemplateView.as_view(template_name="videoedit/index.html"), name="index"),
    path('get_software_info',AllSoftWareInfo.as_view(),name='get_software_info'),
]
