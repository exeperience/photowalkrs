from django.db import models
from django.contrib.auth.models import User
from PhotoWalkr.apps.photos.models import Photo
from PhotoWalkr.apps.profiles.models import GroupProfile
#from PhotoWalkr.photowalks.models import PhotoWalk

FEED_TYPES = (
    ('photo', 'Photo'),
    ('photowalk', 'PhotoWalk'),
    ('group', 'Group'),
)

NOTIFICATION_TYPES = (
    ('follow', 'Follow'),
    ('photo', 'Photo'),
    ('group', 'Group'),
    ('photowalk', 'PhotoWalk'),
)

"""mega feed list, updated for all relevant activities"""
class Feed(models.Model):
    feed_type = models.CharField(choices=FEED_TYPES, max_length=30)
    user = models.ForeignKey(User)
    photowalk = models.ForeignKey('photowalks.Photowalk', blank=True, null=True)
    photo = models.ForeignKey(Photo, blank=True, null=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.user.username

"""created for each user profile"""
class UserWall(models.Model):
    user = models.ForeignKey(User)
    feeds = models.ManyToManyField(Feed, blank=True, null=True)
    def __unicode__(self):
        return self.user.username

class Notification(models.Model):
    notification_type = models.CharField(choices=NOTIFICATION_TYPES, max_length=30)
    user = models.ForeignKey(User, null=True, blank=True, default=None)
    photo = models.ForeignKey(Photo, blank=True, null=True)
    group = models.ForeignKey(GroupProfile, blank=True, null=True)
    photowalk = models.ForeignKey('photowalks.PhotoWalk', blank=True, null=True, default=None)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.notification_type

"""created for each user"""
class UserNotifications(models.Model):
    user = models.ForeignKey(User)
    notify = models.BooleanField(default=False)
    notifications = models.ManyToManyField(Notification, blank=True, null=True) #only if photo is commented or liked
    def __unicode__(self):
        return self.user.username

#class Link(models.Model):
#    user_notifications = models.ForeignKey(UserNotifications, blank=True, null=True)
#    notification = models.ForeignKey(Notification, blank=True, null=True)
#    read = models.BooleanField(default=False)
#    count = models.IntegerField(default=1)
