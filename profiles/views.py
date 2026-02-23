from django.core.files.uploadedfile import UploadedFile
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

# Create your views here.
def store_file(file: UploadedFile):
    with open('temp/image.jpg', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        store_file(request.FILES['image'])

        return HttpResponseRedirect('/profiles')