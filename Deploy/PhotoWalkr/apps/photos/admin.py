from PhotoWalkr.apps.photos.models import Album, Photo, Stats, PhotoInfo
from django.contrib.gis import admin

class AlbumAdmin(admin.ModelAdmin):
    pass

class PhotoAdmin(admin.GeoModelAdmin):
    pass

class StatsAdmin(admin.ModelAdmin):
    pass

class PhotoInfoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Stats, StatsAdmin)
admin.site.register(PhotoInfo, PhotoInfoAdmin)
