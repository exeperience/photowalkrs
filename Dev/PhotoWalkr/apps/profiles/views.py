from forms import UserRegisterForm, GroupRegisterForm
from django.contrib.auth import login, logout
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import GroupProfile, GroupStats, UserProfile
from PhotoWalkr.apps.photowalks.models import PhotoWalk
from PhotoWalkr.apps.photos.models import Photo
from django.core.mail import send_mail

def UserRegistration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            send_mail('Success', 'You have registered successfully!', 'photowalkrs@gmail.com', [ request.POST['email']])
            return HttpResponseRedirect("/signin/")
        return render_to_response("register.html", {'form': form, }, RequestContext(request))
    else:
        form = UserRegisterForm()
        return  render_to_response("register.html", {'form': form, }, RequestContext(request))

def SignIn(request):
    if request.method == 'POST':
        form = auth.forms.AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/photos/all/")
            else:
                return HttpResponse("<h1>Your account has been disabled!</h1>")
        else:
            return HttpResponse("<h1>Your username and password were incorrect.</h1>")
    else:
        form = auth.forms.AuthenticationForm
        return render_to_response("register.html", {'form': form}, RequestContext(request))
    
def SignOut(request):
    logout(request)
    return HttpResponseRedirect("/signin/")

def Group(request, groupid):
	group = GroupProfile.objects.get(id = groupid)
	return render_to_response("group.html", {'group': group}, RequestContext(request))

def GroupTabs(request, groupid, tabid):
    if tabid == '1':
        group = GroupProfile.objects.get(id=groupid)
        return render_to_response("grp-tab1.html", {'group': group}, RequestContext(request))
    elif tabid == '2':
        group = GroupProfile.objects.get(id=groupid)
        return render_to_response("grp-tab2.html", {'group': group}, RequestContext(request))
    elif tabid == '3':
        group = GroupProfile.objects.get(id=groupid)
        return render_to_response("grp-tab3.html", {'group': group}, RequestContext(request))
    elif tabid == '4':
        return HttpResponse("<br/><br/><br/><h2>UnderConstruction</h2>")
    else:
        return HttpResponse("Not Found")

def UserList(request, type, id):
    if type == "group":
        group = GroupProfile.objects.get(id=id)
        Users = group.members.all()
        users = []
        for user in Users:
            users.append(UserProfile.objects.get(user=user))
        print users
        return render_to_response("usrgen.html", { 'users': users } ,RequestContext(request))
    if type == "photowalk":
        photowalk = PhotoWalk.objects.get(id=id)
        users = UserProfile.objects.filter(user__in = photowalk.participants.all())
        return render_to_response("usrgen.html", { 'users': users } ,RequestContext(request))

def GroupsAll(request):
	groups = GroupProfile.objects.all()
	return render_to_response("groups.html",  { 'groups': groups } ,RequestContext(request))

def GroupRegistration(request):
    if request.method == 'POST':
        form = GroupRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect("/groups/all/")
        return render_to_response("genform.html", {'form': form, 'title': "Group Registration"}, RequestContext(request))
    else:
        form = GroupRegisterForm()
        return  render_to_response("genform.html", {'form': form, 'title': "Group Registration"}, RequestContext(request))
