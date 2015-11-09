# -*- coding: utf-8 -*-
"""myBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from article import views as article

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', article.home, name='home'),
    url(r'^index\.html$', article.home, name='index'),
    url(r'^about\.html$', article.about, name='about'),
    url(r'^contact\.html$', article.contact, name='contact'),
    url(r'^blog/article=(?P<pk>\d+)/$', article.blog, name='blog'),
    url(r'^tag/(?P<tag>\w+)/$', article.tag, name='tag'),
    url(r'^category/(?P<cate>\w+)/$', article.category, name='category'),
    url(r'^thanks.html$', article.thanks, name='thanks')
]
