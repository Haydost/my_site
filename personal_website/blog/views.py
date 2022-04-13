from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def starting_page(request):
    return HttpResponse("main page")


def posts(request):
    return HttpResponse("list of posts")


def post_detail(request):
    return HttpResponse("slug passed")
