from django.urls import path, register_converter
from . import views
from . import convecters

register_converter(convecters.FourYearConvector, 'year4')


urlpatterns = [
    path('', views.home),
    path('category/<int:category_id>/', views.category),
    path('archive/<year4:year>/', views.archive)
]