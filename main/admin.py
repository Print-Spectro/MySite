from django.contrib import admin
from .models import Video
from .models import Artwork
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    """fields = ["video_title", "video_published", "video_content"]"""


    fieldsets = [("Title/date", {"fields": ["video_title", "video_published"]}), 
                 ("Content", {"fields": ["video_content"]})
                 ]
    

    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()}

    }

class ArtAdmin(admin.ModelAdmin):
    """fields = [art_title, "art_image", "date_published"]"""

admin.site.register(Video, VideoAdmin)
admin.site.register(Artwork, ArtAdmin)
