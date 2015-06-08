

__author__ = 'shanecrossan'

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
import requests

#Lib

@login_required()
def home(request):
    url = '/' + request.user.username + '/'
    return HttpResponseRedirect(url)

@login_required
def faaa(request):
    if request.user.username != 'faaa':
        return HttpResponseRedirect('/')
    r = requests.get("http://107.170.192.206/tiapiriuf.php")
    text = r.text.encode('ASCII', 'ignore')
    split_text = str.split(text, 'Bornier local')
    value = split_text[0][-5:]
    value_str = str.strip(value, '\x1e')
    value_round = round(float(value_str))

    r2 = requests.get("http://107.170.192.206/socredo.php")
    text2 = r2.text.encode('ASCII', 'ignore')
    split_text2 = str.split(text2, 'Bornier local')
    value2 = split_text2[5][-5:]
    value_str2 = str.strip(value2, '\x1e')
    value_round2 = round(float(value_str2))

    r3 = requests.get("http://107.170.192.206/schmidt.php")
    text3 = r3.text.encode('ASCII', 'ignore')
    split_text3 = str.split(text3, 'Bornier local')
    value3 = split_text3[0][-5:]
    value_str3 = str.strip(value3, '\x1e')
    value_round3 = round(float(value_str3))

    return render_to_response('marie/faaa.html', locals(), context_instance=RequestContext(request))