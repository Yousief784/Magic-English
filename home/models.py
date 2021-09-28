from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
from django.utils.text import slugify


class Video(models.Model):
    name = models.CharField(max_length=100)
    video = EmbedVideoField(null=True,blank=True)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    url = models.URLField(null=True,blank=True)
    image = models.ImageField(upload_to='media/home')
    elsaf = models.ForeignKey('Elsaf', on_delete=models.CASCADE, verbose_name='class', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ('-published_at',)

    def __str__(self):
        return self.name

class Elsaf(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
