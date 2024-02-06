from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse


def home(request):
    return render(request, 'blog/home.html')


def category(request, slug_cat):
    if slug_cat == 'music':
        url_cat = reverse('arch', args=(2024, ))
        return redirect(url_cat)
    return HttpResponse(f'<h1>Category page</h1><p>id:{slug_cat}</p>')


def archive(request, year):
    return HttpResponse(f'<h1>It\'s archive</h1><p>year:{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found:(</h1>')


def about(request):
    return render(request, 'blog/about.html')