from django.shortcuts import render , redirect
from django.views.generic import ListView

from .models import Video, Elsaf
# Create your views here.

def index(request):
    all_elsaf = Elsaf.objects.all()
    all_videos = Video.objects.all()
    return render(request, 'index.html',{'elsaf': all_elsaf, 'all_videos': all_videos})

def all_videos(request, slug):
    all_elsaf = Elsaf.objects.get(slug=slug)
    all_videos = Video.objects.all()
    return render(request, 'all_videos.html', {'videos' : all_videos, 'elsaf' : all_elsaf})

def video_detail(request, id):
    video_detail = Video.objects.get(id=id)
    all_videos = Video.objects.all()
    context={'video': video_detail, 'videos': all_videos}
    return render(request, 'video_detail.html', context)

def SearchPage(request):
    search = request.GET['search']
    videos = Video.objects.filter(name__icontains=search)
    context = {'video': videos, 'search': search}
    return render(request, 'search.html', context)