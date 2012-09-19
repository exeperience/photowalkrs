from PhotoWalkr.apps.photowalks.models import PhotoWalk, PhotoWalkStats
from django.contrib.gis import admin

class PhotoWalkAdmin(admin.GeoModelAdmin):
    pass
    
class PhotoWalkStatsAdmin(admin.GeoModelAdmin):
    pass

admin.site.register(PhotoWalk, PhotoWalkAdmin)
admin.site.register(PhotoWalkStats, PhotoWalkAdmin)
