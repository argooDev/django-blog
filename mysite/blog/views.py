from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Home Page")


def category(request, category_id):
    return HttpResponse(f'<h1>Category page</h1><p>id:{category_id}</p>')


def archive(request, year):
    return HttpResponse(f'<h1>It\'s archive</h1><p>year:{year}</p>')