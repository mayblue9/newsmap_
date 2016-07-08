# coding: utf-8

from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _, ugettext_lazy



class Nodeset(models.Model):
    name = models.CharField(
        verbose_name=ugettext_lazy('node name'),
        max_length=20,
        help_text=ugettext_lazy('Name to display')
    )

    category = models.CharField(
        max_length = 20,
        verbose_name=ugettext_lazy('Group name'),
    )

    isquery = models.BooleanField(
        default=False
    )

    x =models.FloatField(
        default=0
    )
    y =models.FloatField(
        default=0
    )

    indegree_centrality = models.FloatField(
        default = 0
    )

    outdegree_centrality = models.FloatField(
        default = 0
    )

    closeness_centrality = models.FloatField(
        default = 0
    )

    betweenness_centrality = models.FloatField(
        default = 0
    )


    class Meta(object):
        ordering = ['pk']
        verbose_name = ugettext_lazy('Nodeset')
        verbose_name_plural = ugettext_lazy('Nodesets')

    def __unicode__(self):
        return _(self.name)


class NewsData(models.Model):
    Title = models.CharField(
        max_length=200,
        #verbose_name=ugettext_lazy('source name'),
    )

    Date = models.DateTimeField(

    )

    Media = models.CharField(
        max_length=200,
    )

    Url = models.URLField(
        verbose_name=ugettext_lazy('URL'),
        db_index=True, unique=True,
        max_length=200,
        #verbose_name=ugettext_lazy('target name')
    )

    Article = models.TextField(
    )


    class Meta(object):
        #ordering = ('Title',)
        ordering =('Date',)
        verbose_name = ugettext_lazy('New')

    def __unicode__(self):
        return _(self.Title)


"""

class Photo(models.Model):
    image_file = models.ImageField(upload_to='%Y/%m/%d')
    filtered_image_file = models.ImageField(
        null=True,
        upload_to='static_files/uploaded/%Y/%m/%d'
    )
    description = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)




    def delete(self, *args, **kwargs):
        self.image_file.delete()
        self.filtered_image_file.delete()
        super(Photo, self).delete(*args, **kwargs)
    def get_absolute_url(self):
        return reverse_lazy('view_single_photo', kwargs={'photo_id': self.id})
"""






