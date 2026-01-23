from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def january(request):
    return HttpResponse('Don\'t eat any meat.')


def february(request):
    return HttpResponse('Book a restaurant for Valentines\' Day!')