# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from article.models import *

def home(request):
    info = BlogInfo.objects.get(pk = 1)
    return render_to_response('index.html', {'info': info})

def about(request):
    return render_to_response('about.html')

def contact(request):
    return render_to_response('contact.html')

def blog(request, pk):
    blog = Article.objects.get(pk = int(pk))
    return render_to_response('single.html', {'blog': blog})