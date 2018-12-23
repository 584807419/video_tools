from django.urls import path, re_path
from videoedit.views import Hshy, Ajj, Vegas, Pr, Ae, Qsy, Qjj
from django.views.generic import TemplateView
#
urlpatterns = [
    path('', TemplateView.as_view(template_name="videoedit/index.html"), name="index"),
    path('hshy/', Hshy.as_view(), name="hshy"),
    path('ajj/', Ajj.as_view(), name="ajj"),
    path('vegas/', Vegas.as_view(), name="vegas"),
    path('pr/', Pr.as_view(), name="pr"),
    path('ae/', Ae.as_view(), name="ae"),
    path('qsy/', Qsy.as_view(), name="qsy"),
    path('qjj/', Qjj.as_view(), name="qjj"),
]
