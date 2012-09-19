from models import Feed, UserWall, Notification, UserNotifications
from PhotoWalkr.apps.profiles.functions import followers

"""called in as a thread on upload event"""
def create_photo_feed(feed_type, photo, photowalk=1):
    user = photo.user
    feed = Feed(photo=photo, user=user, feed_type=feed_type)
    if feed_type is 'photowalk':
        feed.photowalk = photowalk
    feed.save()
    for stalker in followers(user):
        wall = UserWall.objects.get(user=stalker)
        wall.feeds.add(feed)
        wall.save()
    return

def notify_user( notification_type, user=None, follower=None, photo=None):
    notification = Notification(notification_type=notification_type, user=follower, photo=photo)
    notification.save()
    user_notification = UserNotifications.objects.get(user=user)
    user_notification.notifications.add(notification)
    user_notification.save()
    return

def notify_group(notification_type, group=None, photowalk=None):
    notification = Notification(notification_type=notification_type, group=group, photowalk=photowalk)
    if notification_type is 'group':
        to_notify = group.members.all()
    elif notification_type is 'photowalk':
        to_notify = photowalk.participants.all()
    notification.save()
    for user in to_notify:
        user_notification = UserNotifications.objects.get(user=user)
        user_notification.notifications.add(notification)
        user_notification.save()
    return 
