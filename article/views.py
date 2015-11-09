# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

    articles = Article.objects.all()
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.paginator(paginator.num_pages)

    try:
        categorys = Category.objects.all()
    except Category.DoesNotExist:
        raise Http404

    try:
        tags = Tag.objects.all()
    except Tag.DoesNotExist:
        raise Http404

    return render(request, 'index.html', {'info': info, 'article_list': article_list, 'categorys': categorys, 'tags': tags})

def blog(request, pk):
    try:
        info = BlogInfo.objects.get(pk = 1)
    except BlogInfo.DoesNotExist:
        raise Http404

    try:
        article = Article.objects.get(pk = int(pk))
    except Article.DoesNotExist:
        raise Http404

    try:
        categorys = Category.objects.all()
    except Category.DoesNotExist:
        raise Http404

    try:
        tags = Tag.objects.all()
    except Tag.DoesNotExist:
        raise Http404

    return render(request, 'single.html', {'info': info, 'article': article, 'categorys': categorys, 'tags': tags})

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
            return HttpResponseRedirect('thanks.html')

    try:
        info = BlogInfo.objects.get(pk = 1)
    except BlogInfo.DoesNotExist:
        raise Http404

    return render(request, 'contact.html', {'info': info})

def thanks(request):
    try:
        info = BlogInfo.objects.get(pk = 1)
    except BlogInfo.DoesNotExist:
        raise Http404

    return render(request, 'thanks.html', {'info': info})