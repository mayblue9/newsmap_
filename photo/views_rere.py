# coding: utf-8

from __future__ import unicode_literals

from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    render_to_response,
)

from photo.models import Photo
from photo.forms import PhotoEditForm


## word2vec
from gensim.models import word2vec
import gensim

import simplejson
import decimal

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.http import HttpResponse

##0411_render  to response
#from django.shortcuts import render_to_response





def single_photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)

    return render(
        request,
        'photo.html',
        {
            'photo': photo,
        }
    )


def new_photo(request):
    if request.method == "GET":
        edit_form = PhotoEditForm()
    elif request.method == "POST":
        edit_form = PhotoEditForm(request.POST, request.FILES)

        if edit_form.is_valid():
            new_photo = edit_form.save()

            return redirect(new_photo.get_absolute_url())

    return render(
        request,
        'new_photo.html',
        {
            'form': edit_form,
        }
    )

"""
## word2vec


def parse_array_string(get, name):
    param = get.get(name, None)
    if param == None:
        return []
    else:
        return param.split(",")

#http
#BINARY_WORD2VEC_DATA ="GoogleNews-vectors-negative300.bin" #'GoogleNews-vectors-negative300.bin'
#path
BINARY_WORD2VEC_DATA = 'GoogleNews-vectors-negative300.bin'#'/home/elle/netpowermap/GoogleNews-vectors-negative300.bin'


def word2vec(request):
    model         = gensim.models.word2vec.Word2Vec.load_word2vec_format(BINARY_WORD2VEC_DATA, binary=True)
    positive      = parse_array_string(request.GET, 'pos')
    negative      = parse_array_string(request.GET, 'neg')
    response_data = model.most_similar(positive=positive, negative=negative)
    hashes        = [{"word": d[0], "score": decimal.Decimal(str(d[1]))} for d in response_data]
    model_sim     = model.most_similar(positive=positive ,topn=10)

    return as_json(hashes)
"""

def as_json(variable):
    json = simplejson.dumps(variable)
    return HttpResponse(json, content_type="application/json")

def parse_array_string(get, name):
    param = get.get(name, None)
    if param == None:
        return []
    else:
        return param.split(",")



def search(request):
    errors = []
    if 'word1' in request.GET:
        #q = request.GET['q']
        positive      = request.GET['word1']#['woman','king']
        #negative      = request.GET['word2']#['man']
        if not positive:
            errors.append('Enter a search term.')
        elif len(positive) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            """
            newsbooks = NewsData.objects.filter(Title__icontains=q) #title__icontains=q
            return render_to_response('search_results.html',                #render_to_response
                {'newsbooks': newsbooks, 'query': q})

            """
            #sentences = word2vec.Text8Corpus('text8')
            #model = word2vec.Word2Vec(sentences, size=200)
            #model.save("sample.model")
            """
            sentences = word2vec.Text8Corpus('Stemming.txt')
            model = word2vec.Word2Vec(sentences, size=200)
            model.save("St_sample.model")
            """
            model =word2vec.Word2Vec.load("0419_stemming.model")#word2vec.Word2Vec.load("St_sample.model")#word2vec.Word2Vec.load("ko_word2vec_e.model") #word2vec.Word2Vec.load("sample.model")
            #model = word2vec.Word2Vec.load("ko_word2vec_e.model")

            positive      = request.GET['word1']#['woman','king']
            #negative      = request.GET['word2']#['man']
            response_data  = model.most_similar(positive=positive ,topn=10)
            #response_data = model.most_similar(positive=positive, negative=negative)
            #response_data = model.most_similar(positive=['woman', 'king'], negative= ['man'])
            hashes        = [{"word": d[0], "score": decimal.Decimal(str(d[1]))} for d in response_data]
            model_sim     = model.most_similar(positive=positive ,topn=10)
            json_dump = as_json(hashes)
            print json_dump

            return as_json(hashes)
    return render_to_response('search_form.html',               #render_to_response
        {'errors': errors})


def search1(request):
    errors = []
    if 'word1' in request.GET:
        #q = request.GET['q']
        positive      = request.GET['word1']#['woman','king']
        #negative      = request.GET['word2']#['man']
        if not positive:
            errors.append('Enter a search term.')
        elif len(positive) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            """
            newsbooks = NewsData.objects.filter(Title__icontains=q) #title__icontains=q
            return render_to_response('search_results.html',                #render_to_response
                {'newsbooks': newsbooks, 'query': q})

            """
            #sentences = word2vec.Text8Corpus('text8')
            #model = word2vec.Word2Vec(sentences, size=200)
            #model.save("sample.model")
            #model =word2vec.Word2Vec.load("sample.model")#word2vec.Word2Vec.load("ko_word2vec_e.model") #word2vec.Word2Vec.load("sample.model")
            model = word2vec.Word2Vec.load("sample.model")

            positive      = request.GET['word1']#['woman','king']
            #negative      = request.GET['word2']#['man']
            response_data  = model.most_similar(positive=positive ,topn=2)
            #response_data = model.most_similar(positive=positive, negative=negative)
            #response_data = model.most_similar(positive=['woman', 'king'], negative= ['man'])
            hashes        = [{"word": d[0], "score": decimal.Decimal(str(d[1]))} for d in response_data]
            model_sim     = model.most_similar(positive=positive ,topn=10)
            json_dump = as_json(hashes)
            print json_dump

            #return as_json(hashes)
    return render_to_response('search_form2.html',               #render_to_response
        {'errors': errors})



def index(request):

  return HttpResponse("Hello, world. You're at the polls index.")


##text8 word2vec
def as_json(variable):
    json = simplejson.dumps(variable)
    """
    return render(
            'search_form.html',
            json
    )

    return render_to_response('search_form.html',               #render_to_response
        {'errors': errors})
        """
    return HttpResponse(json, content_type="application/json")

#한글이 깨질때
"""
HttpResponse(
    json_context,
    content_type=u"application/json; charset=utf-8",
    status=status)
"""

def parse_array_string(get, name):
    param = get.get(name, None)
    if param == None:
        return []
    else:
        return param.split(",")


def word2vec(request):
  #sentences = word2vec.Text8Corpus('text8')
  #model = word2vec.Word2Vec(sentences, size=200)
  #model.save("sample.model")
  model = word2vec.Word2Vec.load("0419_stemming.model")

  #positive      = parse_array_string(request.GET, 'pos')
  #negative      = parse_array_string(request.GET, 'neg')
  positive      = request.GET['word1']#['woman','king']
  #negative      = request.GET['word2']#['man']
  response_data = model.most_similar(positive=positive)
  #response_data = model.most_similar(positive=['woman', 'king'], negative= ['man'])
  hashes        = [{"word": d[0], "score": decimal.Decimal(str(d[1]))} for d in response_data]
  model_sim     = model.most_similar(positive=positive ,topn=10)
    #model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)

  ##model save
  #model.save("sample.model")
  #model = word2vec.Word2Vec.load("sample.model")
  return as_json(hashes)
  return render_to_response('search_form.html')



###########0419___new word2vec
def search_word(request):
    errors = []
    if 'word1' in request.GET:
        #q = request.GET['q']
        positive      = request.GET['word1']#['woman','king']
        #negative      = request.GET['word2']#['man']
        if not positive:
            errors.append('Enter a search term.')
        elif len(positive) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            """
            newsbooks = NewsData.objects.filter(Title__icontains=q) #title__icontains=q
            return render_to_response('search_results.html',                #render_to_response
                {'newsbooks': newsbooks, 'query': q})

            """
            #sentences = word2vec.Text8Corpus('text8')
            #model = word2vec.Word2Vec(sentences, size=200)
            #model.save("sample.model")
            model = word2vec.Word2Vec.load("sample.model")#word2vec.Word2Vec.load("ko_word2vec_e.model") #word2vec.Word2Vec.load("sample.model")
            #model = word2vec.Word2Vec.load("ko_word2vec_e.model")

            positive      = request.GET['word1']#['woman','king']
            #negative      = request.GET['word2']#['man']
            response_data  = model.most_similar(positive=positive ,topn=2)
            #response_data = model.most_similar(positive=positive, negative=negative)
            #response_data = model.most_similar(positive=['woman', 'king'], negative= ['man'])
            hashes        = [{"word": d[0], "score": decimal.Decimal(str(d[1]))} for d in response_data]
            model_sim     = model.most_similar(positive=positive ,topn=10)
            return as_json(hashes)
    return render_to_response('search_form2.html',               #render_to_response
        {'errors': errors})





#########################search form test 0411
def search_form1(request) :
    return render_to_response('search_form.html')


