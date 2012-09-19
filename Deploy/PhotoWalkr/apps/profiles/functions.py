#from django.contrib.auth.models import User
from PhotoWalkr.apps.feeds.models import UserWall, UserNotifications
from PhotoWalkr.apps.profiles.models import Following

def create_user_wall(user):
    wall = UserWall(user=user)
    notifications = UserNotifications(user=user)
    wall.save()
    notifications.save()

def follow(stalker, victim):
    if is_following(stalker, victim):
        return
    follow = Following(user = stalker, following = victim)
    reverse = Following.objects.filter(user=victim, following=stalker)
    if reverse:
        follow.mutual = reverse[0].mutual = True
        reverse[0].save()
    follow.save()

def unfollow(stalker, victim):
    follow = Following.objects.get(user = stalker, following = victim)
    reverse = Following.objects.filter(user=victim, following=stalker)
    if reverse:
        follow.mutual = reverse[0].mutual = False
        reverse[0].save()
    follow.delete()

def followers(user):
    followings = Following.objects.filter(following=user)
    followers = []
    for following in followings:
        followers.append(following.user)
    return followers

def is_following(stalker, victim):
    if Following.objects.filter(user=stalker, following=victim):
        return True
    return False

"""mutual following"""
def friends(user):
    _list = Following.objects.filter(user=user, mutual=True)
    friends = []
    for friend in _list:
        friends.append(friend.following)
    return friends

"""GROUPS"""

def members(group):
    return group.members.all()

def add_member(group, user):
    group.members.add(user)
    group.save()

def remove_member(group, user):
    group.members.remove(user)
    group.save()
