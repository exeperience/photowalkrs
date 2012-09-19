from PhotoWalkr.apps.feeds.models import Feed, UserWall, Notification, UserNotifications
from django.contrib import admin

class FeedAdmin(admin.ModelAdmin):
    pass

class UserWallAdmin(admin.ModelAdmin):
    pass

class NotificationAdmin(admin.ModelAdmin):
    pass

class UserNotificationsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Feed, FeedAdmin)
admin.site.register(UserWall, UserWallAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(UserNotifications, UserNotificationsAdmin)
