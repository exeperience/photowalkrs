from django.conf.urls.defaults import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib.gis import admin
from PhotoWalkr.apps.photos.views import UploadPhoto, Photos, ViewPhoto, LikePhoto, testload, PhotoList
from PhotoWalkr.apps.profiles.views import UserRegistration, SignIn, SignOut, Group, GroupsAll, GroupTabs, UserList, GroupRegistration
from PhotoWalkr.apps.photowalks.views import PhotoWalksAll, CreatePhotoWalk, ViewPhotoWalk, PhotoWalkList, PhotoWalkTabs, PhotoWalkPhotos
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', Photos),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^like/photo/(?P<photoid>\w*?)/$', LikePhoto),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/', UploadPhoto),
    url(r'^testload/', testload),
    url(r'^photos/(?P<tab>\w*?)/$', Photos),
    url(r'^photowalks/all/', PhotoWalksAll),
    url(r'^photowalks/create/', CreatePhotoWalk),
    url(r'^group/(?P<groupid>\w*?)/$', Group),
    url(r'^group/(?P<groupid>\w*?)/(?P<tabid>\w*?)/$', GroupTabs),
    url(r'^userlist/(?P<type>\w*?)/(?P<id>\w*?)/$', UserList),
    url(r'^photolist/(?P<type>\w*?)/(?P<gid>\w*?)/$', PhotoList),
    url(r'^photolist/(?P<type>\w*?)/(?P<pwid>\w*?)/(?P<uid>\w*?)/$', PhotoList),
    url(r'^photowalk/(?P<id>\w*?)/$', ViewPhotoWalk),
    url(r'^photowalk/(?P<pwid>\w*?)/tab/(?P<tabid>\w*?)/', PhotoWalkTabs),
    url(r'^photowalk/(?P<pwid>\w*?)/user/(?P<uid>\w*?)/', PhotoWalkPhotos),
    url(r'^photowalklist/(?P<type>\w*?)/(?P<gid>\w*?)/$', PhotoWalkList),
    url(r'^groups/all/', GroupsAll),
    url(r'^signin/', SignIn),
    url(r'^signout/', SignOut),
    url(r'^register/', UserRegistration),
    url(r'^groupregister/', GroupRegistration),
    url(r'^photo/(?P<photoid>\w*?)/$', ViewPhoto),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
