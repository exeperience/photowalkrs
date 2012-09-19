from django import forms
from models import UserProfile, UserStats, GroupProfile, GroupStats
from django.contrib.auth.models import User
from django.contrib.admin.widgets import FilteredSelectMultiple

class UserRegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget = forms.PasswordInput, label="Confirm Password")
    display_image = forms.ImageField(required=False)
    email = forms.EmailField()
    def save(self):
        profile = UserProfile()
        stats = UserStats()
        stats.save()
        username = self.cleaned_data["username"]
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        display_image = self.cleaned_data["display_image"]
        if display_image is None:
            admin = UserProfile.objects.get(id=1)
            display_image = admin.display_image
        profile.user = User.objects.create_user(username, email, password)
        profile.display_image = display_image
        profile.stats = stats
        profile.save()

class GroupRegisterForm(forms.Form):
    name = forms.CharField()
    info = forms.CharField(widget=forms.Textarea)
    display_image = forms.ImageField()
    location = forms.CharField()
    members = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=FilteredSelectMultiple("verbose name", is_stacked=False))
    def save(self, user):
        group = GroupProfile()
        group.admin = user
        group.name = self.cleaned_data["name"]
        group.info = self.cleaned_data["info"]
        group.location_text = self.cleaned_data["location"]
        group.display_image = self.cleaned_data["display_image"]
        stats = GroupStats()
        stats.num_members = len(self.cleaned_data["members"])
        stats.save()
        group.stats = stats
        group.save()
        group.members.add(*self.cleaned_data["members"])
        group.save()
