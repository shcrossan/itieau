

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
    r = requests.get("http://107.170.192.206/test.php")
    text = r.text.encode('ASCII', 'ignore')
    str_text = str(text)
    split_text = str.split(text, 'Bornier local')
    value = split_text[0][-5:]

    return render_to_response('home.html', locals(), context_instance=RequestContext(request))