

__author__ = 'shanecrossan'

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
import requests

#Lib



@login_required
def home(request):
    r = requests.get("http://107.170.192.206/tiapiriuf.php")
    text = r.text.encode('ASCII', 'ignore')
    split_text = str.split(text, 'Bornier local')
    value = split_text[0][-5:]
    value_round = int(round(value, 0))

    r2 = requests.get("http://107.170.192.206/socredo.php")
    text2 = r2.text.encode('ASCII', 'ignore')
    split_text2 = str.split(text2, 'Bornier local')
    value2 = split_text2[5][-5:]

    r3 = requests.get("http://107.170.192.206/schmidt.php")
    text3 = r3.text.encode('ASCII', 'ignore')
    split_text3 = str.split(text3, 'Bornier local')
    value3 = split_text3[0][-5:]

    return render_to_response('home.html', locals(), context_instance=RequestContext(request))