from django.urls import path

from . import views

app_name = 'home'


urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('business/', views.business, name='business'),
    path('rnd/', views.rnd, name='rnd'),
    path('service/', views.service, name='service'),
]
