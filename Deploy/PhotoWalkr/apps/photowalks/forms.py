from django.forms import ModelForm
from models import PhotoWalk, PhotoWalkStats
from PhotoWalkr.apps.photos.models import Album

class PhotoWalkForm(ModelForm):
    class Meta:
        model = PhotoWalk
        exclude = ('photo', 'admin', 'album', 'tags', 'status', 'stats',)
    def save(self, user):
        photowalk = super(PhotoWalkForm, self).save(commit=False)
        stats = PhotoWalkStats()
        stats.save()
        album = Album()
        album.user = user
        album.save()
        photowalk.album = album
        photowalk.admin = user
        photowalk.stats = stats
        photowalk.save()

        