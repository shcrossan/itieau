

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
    value_str = str.strip(value, '\x1e')
    value_split = str.split(value_str, '.')
    if int(value_split[1]) >= 50:
        value_round = int(value_split[0]) + 1
    else:
        value_round = value_split[0]

    r2 = requests.get("http://107.170.192.206/socredo.php")
    text2 = r2.text.encode('ASCII', 'ignore')
    split_text2 = str.split(text2, 'Bornier local')
    value2 = split_text2[5][-5:]
    value_str2 = str.strip(value2, '\x1e')
    value_split2 = str.split(value_str2, '.')
    if int(value_split2[1]) >= 50:
        value_round2 = int(value_split2[0]) + 1
    else:
        value_round2 = value_split2[0]

    r3 = requests.get("http://107.170.192.206/schmidt.php")
    text3 = r3.text.encode('ASCII', 'ignore')
    split_text3 = str.split(text3, 'Bornier local')
    value3 = split_text3[0][-5:]
    value_str3 = str.strip(value3, '\x1e')
    value_split3 = str.split(value_str3, '.')
    if int(value_split3[1]) >= 50:
        value_round3 = int(value_split3[0]) + 1
    else:
        value_round3 = value_split3[0]

    return render_to_response('home.html', locals(), context_instance=RequestContext(request))