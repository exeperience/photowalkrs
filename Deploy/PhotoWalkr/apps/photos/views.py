from PhotoWalkr import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from PhotoWalkr.apps.profiles.models import UserProfile, GroupProfile
from PhotoWalkr.apps.photowalks.models import PhotoWalk
from PhotoWalkr.apps.photos.functions import GroupPhotos, PhotoWalkPhotos
from django.contrib.auth.models import User


#--------------VIEWS---------------------
from forms import PhotoForm
from django.template import RequestContext
from models import Photo, Stats
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def Photos(request, tab='all'):
    # add filter for tabs
    # ....
    photo_list = Photo.objects.all()
    for photo in photo_list:
        photo.userprofile = UserProfile.objects.get(user=photo.user)
    paginator = Paginator(photo_list, 21)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        photos = paginator.page(page)
    except (EmptyPage, InvalidPage):
        photos = paginator.page(paginator.num_pages)

    return render_to_response('photos.html', {"photos": photos, 'MEDIA_URL':settings.MEDIA_URL, 'STATIC_URL': settings.STATIC_URL,}, RequestContext(request))

def UploadPhoto(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect("/upload/")
        else:
            return render_to_response("upload.html", {'form': form, 'STATIC_URL': settings.STATIC_URL,}, RequestContext(request))
    form = PhotoForm()
    return render_to_response("upload.html", {'form': form, 'STATIC_URL': settings.STATIC_URL,}, RequestContext(request))

def testload(request):
    photo_list = Photo.objects.all()
    for photo in photo_list:
        stat = Stats.objects.get(photo = photo)
        photo.stats = stat
        photo.userprofile = UserProfile.objects.get(user=photo.user)
    paginator = Paginator(photo_list, 21)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        photos = paginator.page(page)
    except (EmptyPage, InvalidPage):
        photos = paginator.page(paginator.num_pages)

    return render_to_response('1.html', {"photos": photos, 'MEDIA_URL':settings.MEDIA_URL, 'STATIC_URL': settings.STATIC_URL,}, RequestContext(request))

def ViewPhoto(request, photoid):
    photo = Photo.objects.get(id=photoid)
    user = UserProfile.objects.get(user=photo.user)
    photo.userphotos = Photo.objects.filter(user=photo.user)
    photo.userprofile = user
    if photo.stats.is_photowalks:
        photowalk = PhotoWalk.objects.get(album__photos__in = [photo,])
        photo.photowalk = photowalk
        photowalkphotos = photowalk.album.photos.all()
        photo.photowalkphotos = photowalkphotos
    try:
        stat = Stats.objects.get(photo=photo)
        stat.views += 1
        stat.save()
    except:
        pass
    if request.method == 'POST':
        return HttpResponseRedirect('')
    c = {'photo':photo,}
    c.update(csrf(request))
    return render_to_response('photo.html', c, RequestContext(request))

def PhotoList(request, type, gid=-1, pwid=-1, uid=-1):
    if(type == "group"):
        group = GroupProfile.objects.get(id=gid)
        photos = GroupPhotos(group)
        return render_to_response("phgen.html", { 'photos': photos } ,RequestContext(request))
    if(type == "photowalk"):
        if uid == "0":
            photos = Photo.objects.filter(album__photowalk=PhotoWalk.objects.get(id=pwid))
        else:
            photos = Photo.objects.filter(album__photowalk=PhotoWalk.objects.get(id=pwid), user = User.objects.get(id=uid))
        return render_to_response("phgen.html", { 'photos': photos } ,RequestContext(request))

def LikePhoto(request, photoid):
    photo = Photo.objects.get(id = photoid)
    try:
        stat = Stats.objects.get(photo=photo)
        stat.likes += 1
        stat.save()
    except:
        pass