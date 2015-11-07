# -*- coding: utf-8 -*-
from django.contrib import admin
from article.models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date')    #Setting display fields
    search_fields = ['title']                       #Setting search fields
    list_filter = ('date',)                         #Setting filter by post date
    filter_horizontal = ('tag',)                    #Horizontal display tag's select field


class InfoAdmin(admin.ModelAdmin):
    list_display = ('blogName', 'oName', 'intro')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)

admin.site.register(BlogInfo, InfoAdmin)
