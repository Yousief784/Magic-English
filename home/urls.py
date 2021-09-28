from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:slug>', views.all_videos, name='all_video'),
    path('post/<int:id>', views.video_detail, name='video_detail'),
    path('result/', views.SearchPage, name='search'),


]