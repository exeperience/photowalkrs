from PhotoWalkr.apps.profiles.models import UserProfile, GroupProfile, Following, UserStats, GroupStats
from django.contrib.gis import admin

class UserProfileAdmin(admin.GeoModelAdmin):
    pass

class GroupProfileAdmin(admin.GeoModelAdmin):
    pass

class FollowingAdmin(admin.ModelAdmin):
    pass

class UserStatsAdmin(admin.ModelAdmin):
    pass

class GroupStatsAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Following, FollowingAdmin)
admin.site.register(GroupProfile, GroupProfileAdmin)
admin.site.register(GroupStats, GroupStatsAdmin)
admin.site.register(UserStats, UserStatsAdmin)
