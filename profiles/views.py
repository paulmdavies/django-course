from django.core.files.uploadedfile import UploadedFile
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from profiles.forms import ProfileForm
from profiles.models import UserProfile


# Create your views here.
class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm
        return render(
            request,
            "profiles/create_profile.html",
            {
                'form': form
            }
        )

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            UserProfile(image=request.FILES['user_image']).save()
            return HttpResponseRedirect('/profiles')

        return render(
            request,
            "profiles/create_profile.html",
            {
                'form': submitted_form
            }
        )