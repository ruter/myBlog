# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from article.models import *
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


def home(request):
    try:
        info = BlogInfo.objects.get(pk = 1)
    except BlogInfo.DoesNotExist:
        raise Http404

    try:
        article_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'index.html', {'info': info, 'article_list': article_list})

def blog(request, pk):
    try:
        info = BlogInfo.objects.get(pk = 1)
    except BlogInfo.DoesNotExist:
        raise Http404

    try:
        article = Article.objects.get(pk = int(pk))
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'single.html', {'info': info, 'article': article})

def category(request, cate):
    try:
        info = BlogInfo.objects.get(pk = 1)
    except BlogInfo.DoesNotExist:
        raise Http404

    try:
        article_list = Article.objects.filter(category__name__iexact=cate)
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'tag.html', {'info': info, 'article_list': article_list, 'article_tag': cate})

def tag(request, tag):
    try:
        info = BlogInfo.objects.get(pk = 1)
    except BlogInfo.DoesNotExist:
        raise Http404

    try:
        article_list = Article.objects.filter(tag__tag__iexact=tag) # Query related value
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'info': info, 'article_list': article_list, 'article_tag': tag})

def about(request):
    try:
        info = BlogInfo.objects.get(pk = 1)
    except BlogInfo.DoesNotExist:
        raise Http404

    return render(request, 'about.html', {'info': info})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('contact.html')
        
    try:
        info = BlogInfo.objects.get(pk = 1)
    except BlogInfo.DoesNotExist:
        raise Http404

    return render(request, 'contact.html', {'info': info})