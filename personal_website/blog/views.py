from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def f_1(request):
    return HttpResponse("main page")


def f_2(request):
    return HttpResponse("list of posts")
