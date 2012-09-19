from django.contrib.gis.db import models
from django.contrib.auth.models import User
from tagging.fields import TagField
from PhotoWalkr.apps.photos.models import Album, Photo
from PhotoWalkr.settings import SRID
import datetime
#from PhotoWalkr.profiles.models import GroupProfile

PW_STATUS = (
    ('future', 'Future'),
    ('present', 'Present'),
    ('history','History'),
)

class PhotoWalkStats(models.Model):
    score = models.IntegerField(default=0, blank=True)
    likes = models.IntegerField(default=0, blank=True)
    liked_by = models.ManyToManyField(User, blank=True, null=True)
    views = models.IntegerField(default=0, blank=True)
    num_participants = models.IntegerField(default=0, blank=True)

class PhotoWalk(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ForeignKey(Photo, blank=True, null=True)
    admin = models.ForeignKey(User, related_name="as_suggestion_pw")
    group = models.ForeignKey('profiles.GroupProfile', blank=True, null=True)
    album = models.ForeignKey(Album, blank=True, null=True) #created at creation of instance
    description = models.TextField()
    #location = models.PointField(srid=SRID, null=True, default=None)
    location = models.TextField(blank=True, null=True)
    objects = models.GeoManager()
    participants = models.ManyToManyField(User, blank=True, null=True)
    tags = TagField()
    status = models.CharField(choices = PW_STATUS, max_length=30)
    date = models.DateTimeField(default=datetime.datetime(2012, 8, 4, 12, 30, 45))
    stats = models.ForeignKey(PhotoWalkStats, blank=True, null=True)
    def __unicode__(self):
        return self.name
    

