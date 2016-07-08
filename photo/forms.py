# coding: utf-8

from __future__ import unicode_literals

from django import forms

from photo.models import Photo


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image_file', 'description', )
        # exclude = ('filtered_image_file',)


## add 04_22

class SearchForm(forms.Form):

    '''
    Text searching form.
    '''
    # pylint: disable=C0103
    q = forms.CharField(
        label='검색어',
        min_length=1,
        required=False,
    )
    period = forms.ChoiceField(
        label='기간',
        required=False,
        choices=(
            ('1w', '1주'),
            ('1m', '1개월'),
            ('5m', '5개월'),
        ),
        initial=False
    )
    every = forms.BooleanField(
        label='전체',
        required=False,
        initial=True
    )
    pol = forms.BooleanField(
        label='정치인',
        required=False,
        initial=False
    )
    pub = forms.BooleanField(
        label='공공기관',
        required=False,
        initial=False
    )
    ent = forms.BooleanField(
        label='기업',
        required=False,
        initial=False
    )
    univ = forms.BooleanField(
        label='대학/기관',
        required=False,
        initial=False
    )


