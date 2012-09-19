from django.contrib.gis.db import models
from django.contrib.auth.models import User
from PhotoWalkr.apps.photowalks.models import PhotoWalk
from tagging.fields import TagField
from PhotoWalkr.settings import SRID

class UserStats(models.Model):
    score = models.IntegerField(default=0, blank=True)
    likes = models.IntegerField(default=0, blank=True)
    liked_by = models.ManyToManyField(User, blank=True, null=True, related_name="likers")
    views = models.IntegerField(default=0, blank=True)

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    display_image = models.ImageField(upload_to='photos/dp/user', blank=True, null=True, default='photos/dp/user/HsTZSDw4avx.gif')
    photowalk_suggestions = models.ManyToManyField(PhotoWalk, blank=True, null=True, related_name="as_suggestion_u")
    photowalks = models.ManyToManyField(PhotoWalk, blank=True, null=True, related_name="as_photowalk_u")
    info = models.TextField()
    tags = TagField()
    location = models.PointField(srid=SRID, blank=True, null=True)
    objects = models.GeoManager()
    stats = models.ForeignKey(UserStats, null=True, blank=True)
    def __unicode__(self):
        return self.user.username

class GroupStats(models.Model):
    score = models.IntegerField(default=0, blank=True)
    num_members = models.IntegerField(default = 0, blank=True)
    num_photos = models.IntegerField(default = 0, blank=True)
    num_photowalks = models.IntegerField(default = 0, blank=True)
    likes = models.IntegerField(default=0, blank=True)
    liked_by = models.ManyToManyField(User, blank=True, null=True)
    views = models.IntegerField(default=0, blank=True)
    num_members = models.IntegerField(default=0, blank=True)

class GroupProfile(models.Model):
    name = models.CharField(max_length=30)
    admin = models.ForeignKey(User, related_name="as_group_admin", default=1)
    info = models.TextField()
    members = models.ManyToManyField(User, related_name="as_member", blank=True, null=True)
    display_image = models.ImageField(upload_to='photos/dp/group', blank=True, null=True)
    photowalk_suggestions = models.ManyToManyField(PhotoWalk, blank=True, null=True, related_name="as_suggestion")
    tags = TagField()
    location = models.PointField(srid=SRID, blank=True, null=True)
    location_text = models.TextField(blank=True, null=True)
    objects = models.GeoManager()
    stats = models.ForeignKey(GroupStats, null=True, blank=True, default=None)
    def __unicode__(self):
        return self.name

class Following(models.Model):
    user = models.ForeignKey(User, related_name="stalker")
    following = models.ForeignKey(User, related_name="victim")
    """ is set when mutual following """
    mutual = models.BooleanField(default=False)
    class Meta:
        unique_together = (("user", "following"),)
    def __unicode__(self):
        return self.user.username
