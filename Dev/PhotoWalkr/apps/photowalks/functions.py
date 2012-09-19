#from models import PhotoWalk
from PhotoWalkr.apps.photowalks.models import PhotoWalk, PhotoWalkStats
from django.contrib.auth.models import User
from time import strptime, mktime
import datetime

def create_photowalk(data):
    stats = PhotoWalkStats()
    stats.save()
    walk = PhotoWalk()
    walk.name = data["pwname"]
    walk.admin = User.objects.get(pk=data["adminid"])
    dt = strptime(data["pw-datetime"], "%A, %B %d, %Y at %I:%M %p")
    walk.date = datetime.datetime.fromtimestamp(mktime(dt))
    walk.stats = stats
    walk.save()
    return


def invite_user(photowalk, user):
    profile = user.get_profile()
    profile.photowalk_suggestions.add(photowalk)
    profile.save()
    return

"""group functions"""
def suggest_photowalk(photowalk, user):
    group = photowalk.group
    group.photowalk_suggestions.add(photowalk)
    group.save()
    
def approve_photowalk_group(photowalk, admin):
    group = photowalk.group
    group.photowalks.add(photowalk)
    group.photowalk_suggestions.remove(photowalk)
    group.save()
    return

def remove_suggested_photowalk(photowalk, admin):
    group = photowalk.group
    group.photowalk_suggestions.remove(photowalk)
    group.save()
    ul = photowalk.participants.all()
    for usr in ul:
        profile = usr.get_profile()
        profile.photowalks.remove(photowalk)
        profile.photowalk_suggestions.remove(photowalk)
        profile.save()
    return

def join_photowalk(photowalk, user):
    photowalk.participants.add(user)
    profile = user.get_profile()
    profile.photowalk_suggestions.remove(photowalk)
    profile.photowalks.add(photowalk)
    profile.save()
    photowalk.save()

def unjoin_photowalk(photowalk, user):
    photowalk.participants.remove(user)
    profile = user.get_profile()
    profile.photowalks.remove(photowalk)
    profile.save()
    photowalk.save()