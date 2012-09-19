from django.forms import ModelForm
from django import forms
from models import Photo, Stats, PhotoInfo

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        exclude = ('location', 'taken', 'user', 'info', 'notification_enabled', 'tags', 'stats',)
    def save(self, user):
        photo = super(PhotoForm, self).save(commit=False)
        stats = Stats()
        stats.save()
        info = PhotoInfo()
        info.save()
        photo.stats = stats
        photo.info = info
        photo.user = user
        photo.save()
        
