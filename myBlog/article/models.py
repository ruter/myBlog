from django.db import models

class Category(models.Model):
    name = models.CharField(u'Name', max_length=50)                 #Category's name

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Tag(models.Model):
    tag = models.CharField(u'Tag', max_length=20)                   #Tag

    def __unicode__(self):
        return self.tag

    class Meta:
        ordering = ['tag']


class Article(models.Model):
    title = models.CharField(u'Title', max_length=50)               #Article's title
    content = models.TextField(u'Content')                          #Article's content
    tag = models.ManyToManyField(Tag, blank=True)                   #Article's tags
    category = models.ForeignKey('Category', blank=True, null=True) #Article's category
    date = models.DateField(u'Date', auto_now_add=True)             #Article's post date

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date']                                        #Ordering by date desc


class BlogInfo(models.Model):
    blogName = models.CharField(u'Blog Name', max_length=20)        #Blog's name
    logo = models.CharField(u'Logo', max_length=100, blank=True, null=True)         #Logo's link
    avatar = models.CharField(u'Avatar', max_length=100, blank=True, null=True)     #Your avatar's link
    oName = models.CharField(u'Name', max_length=20, blank=True, null=True)         #Your name
    intro = models.TextField(u'Intro', blank=True, null=True)       #Your intro