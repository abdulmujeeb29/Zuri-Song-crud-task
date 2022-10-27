from django.contrib import admin

from musicapp.models import Artiste, Lyric, Song

# Register your models here.
admin.site.register(Artiste),
admin.site.register(Song),
admin.site.register(Lyric)