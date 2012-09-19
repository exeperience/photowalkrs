from models import Stats
from PhotoWalkr.apps.photowalks.models import PhotoWalk
from PhotoWalkr.apps.profiles.models import UserProfile
from PhotoWalkr import settings
from PhotoWalkr.apps.feeds.functions import create_photo_feed, notify_group, notify_user
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

#-----------------HELPER---------------------------

def geo(request):
    waypoints = PhotoWalk.objects.all()
    return render_to_response('geo.html', {'waypoints':waypoints,},)

def add_to_album(photo, album):
    if album.is_photowalk_album is True:
        create_photo_feed(photo=photo, feed_type='photowalk', photowalk=PhotoWalk.objects.get(album=album))
    else:
        create_photo_feed(photo=photo, feed_type='photo')
    album.photos.add(photo)
    album.save()

def remove_from_album(photo, album):
    album.photos.remove(photo)
    album.save()

def has_liked(user, photo):
    if Stats.objects.filter(liked_by__in = [user], photo = photo):
        return True
    return False

def like_photo(user, photo):
    if has_liked(user, photo):
        return
    stat = Stats.objects.get(photo=photo)
    stat.likes += 1
    stat.liked_by.add(user)
    stat.save()
    notify_user(notification_type='photo', photo=photo, user=user)

def unlike_photo(user, photo):
    if not has_liked(user, photo):
        return
    stat = Stats.objects.get(photo=photo)
    stat.likes -= 1
    stat.liked_by.remove(user)
    stat.save()

def PhotoWalkPhotos(photowalk):
    album = photowalk.album
    photos = album.photos.all()
    for photo in photos:
        photo.photowalk = photowalk
        photo.userprofile = UserProfile.objects.get(user=photo.user)
    return photos

def GroupPhotos(group):
    photos = []
    photowalks = PhotoWalk.objects.filter(group=group)
    for photowalk in photowalks:
        photos += PhotoWalkPhotos(photowalk)
    return photos


