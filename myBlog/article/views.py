# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from article.models import *
from django import forms
from django.template import RequestContext


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


def home(request):
    info = BlogInfo.objects.get(pk = 1)
    return render(request, 'index.html', {'info': info})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('contact.html')

    return render(request, 'contact.html')

def blog(request, pk):
    blog = Article.objects.get(pk = int(pk))
    return render(request, 'single.html', {'blog': blog})
