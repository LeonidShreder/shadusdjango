from django.conf.urls import include, url
from django.contrib import admin
from article.views import template_two, template_three_simple

from article import views
urlpatterns = [
    url(r'^1/', views.basic, name='basic'),
    url(r'^2/', views.template_two, name='two'),
    url(r'^3/', views.template_three_simple, name='three'),
]
