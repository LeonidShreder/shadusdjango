from django.conf.urls import include, url
from django.contrib import admin
from article.views import template_two, template_three_simple


from article import views
urlpatterns = [
    url(r'^1/', views.basic, name='basic'),
    url(r'^2/', views.template_two, name='two'),
    url(r'^3/', views.template_three_simple, name='three'),
    url(r'^articles/all/$', views.articles),
    url(r'^articles/get/(?P<article_id>\d+)/$', views.article, name='article'),
    url(r'^articles/addlike/(?P<article_id>\d+)/$', views.addlike, name='addLike'),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', views.addcomment, name='addcomment'),
    url(r'^$', views.articles, name='articles'),
]
