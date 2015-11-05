from django.db import models

class Category(models.Model):
    name = models.CharField(u'Name', max_length=50)                 #Category's name

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(u'Title', max_length=50)               #Article's title
    content = models.TextField(u'Content')                          #Article's content
    date = models.DateField(u'Date', auto_now_add=True)             #Article's post date
    category = models.ForeignKey('Category', blank=True, null=True) #Article's category

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date']                                        #Ordering by date desc
