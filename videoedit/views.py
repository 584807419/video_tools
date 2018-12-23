from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import VideoEditSoftware


class Hshy(View):
    def get(self, request):
        return render(request, 'videoedit/index.html', {"software_queryset":VideoEditSoftware.objects.filter(name__icontains="会声会影")})

class Ajj(View):
    def get(self, request):
        return render(request, 'videoedit/index.html', {"software_queryset":VideoEditSoftware.objects.filter(name__icontains="爱剪辑")})

class Vegas(View):
    def get(self, request):
        return render(request, 'videoedit/index.html', {"software_queryset":VideoEditSoftware.objects.filter(name__icontains="vegas")})

class Pr(View):
    def get(self, request):
        return render(request, 'videoedit/index.html', {"software_queryset":VideoEditSoftware.objects.filter(name__icontains="premiere")})

class Ae(View):
    def get(self, request):
        return render(request, 'videoedit/index.html', {"software_queryset":VideoEditSoftware.objects.filter(name__icontains="effects")})

class Qsy(View):
    def get(self, request):
        return render(request, 'videoedit/index.html', {"software_queryset":VideoEditSoftware.objects.filter(name__icontains="水印")})

class Qjj(View):
    def get(self, request):
        return render(request, 'videoedit/index.html', {"software_queryset":VideoEditSoftware.objects.filter(name__icontains="快剪辑")})

