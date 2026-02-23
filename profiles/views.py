from django.core.files.uploadedfile import UploadedFile
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from profiles.models import UserProfile


# Create your views here.
class CreateProfileView(CreateView):
    template_name = 'profiles/create_profile.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/profiles'


class ProfilesView(ListView):
    template_name = 'profiles/user_profiles.html'
    model = UserProfile
    context_object_name = 'profiles'