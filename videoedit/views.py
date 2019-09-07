from django.shortcuts import render

from django.views import View
from .models import VideoEditSoftware


class AllSoftWareInfo(View):
    def get(self, request):
        pk = int(request.GET.get('pk'))
        return render(
            request,
            'videoedit/index.html',
            {'software_queryset': VideoEditSoftware.objects.filter(pk=pk),
             'videoedit_software_info': VideoEditSoftware.objects.all().order_by('name')
             }
        )
