from django.urls import path, register_converter
from . import views
from . import convecters

register_converter(convecters.FourYearConvector, 'year4')


urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug_cat>/', views.category, name='category'),
    path('about/', views.about, name='about'),
    path('archive/<year4:year>/', views.archive, name='arch')
]