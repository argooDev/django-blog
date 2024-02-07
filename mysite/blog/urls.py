from django.urls import path, register_converter
from . import views
from . import convecters

register_converter(convecters.FourYearConvector, 'year4')


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', views.show_post, name='post'),
]