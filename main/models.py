from django.db import models
from datetime import datetime
# Create your models here.
class Video(models.Model):
    video_title = models.CharField(max_length=200)
    video_content = models.TextField()
    video_published = models.DateTimeField("date published", default=datetime.now())

    def __str__(self):
        return self.video_title
    
class Artwork(models.Model):
    art_title = models.CharField(max_length = 200)
    art_published = models.DateTimeField("date published", default=datetime.now())
    art_image = models.ImageField()

    def __str__(self):
        return self.art_title