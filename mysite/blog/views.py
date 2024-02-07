from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.defaultfilters import slugify

data_db = [
    {'id': 1, 'name': 'Alex', 'email': 'Email_alex'},
    {'id': 2, 'name': 'Bob', 'email': 'Email_bob'},
    {'id': 3, 'name': 'John', 'email': 'Email_John'},
    {'id': 4, 'name': 'Mike', 'email': 'Email_Mike'},
]

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]


def home(request):
    home_template = {
        'title': 'Home page',
        'posts': data_db,
    }
    return render(request, 'blog/home.html', home_template)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About page'})


def show_post(request, post_id):
    return HttpResponse(f'Person has id: {post_id}')


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")
