from django.contrib import admin
from .models import Artist,Album,MediaType,Genre,Track
# Register your models here.
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(MediaType)
admin.site.register(Genre)
admin.site.register(Track)