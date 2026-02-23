from django.core.files.uploadedfile import UploadedFile
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from profiles.forms import ProfileForm


# Create your views here.
def store_file(file: UploadedFile):
    with open('temp/image.jpg', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


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
            store_file(request.FILES['image'])
            return HttpResponseRedirect('/profiles')

        return render(
            request,
            "profiles/create_profile.html",
            {
                'form': submitted_form
            }
        )