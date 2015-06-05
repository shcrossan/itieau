

__author__ = 'shanecrossan'

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
import requests

#Lib
import base64
from mechanize import Browser


@login_required
def home(request):
    # user = 'S500'
    # pwd = 'ADMINI'
    # url = 'http://tiapiriuf.dyndns.info/BDY_Data.htm?p0=101&p1=100&p2=7&p3=8&p4=45&p5=48&p6=9&p7=10&p8=94&p9=41&p10=46&p11=49&p12=25&p13=160&p14=63&p15=66&p16=28&p17=42'
    # browser = Browser()
    # browser.addheaders.append(('Authorization', 'Basic %s' % base64.encodestring('%s:%s' % (user, pwd))))
    headers = {'Content-Length': '160'}
    r = requests.get("http://107.170.192.206/test.php", headers=headers)
    status_code = r.status_code
    header = r.headers
    text = r.text.encode('ASCII', 'ignore')
    str_text = str(text)
    split_text = str.split(text, 'Bornier local')
    value = split_text[0][-5:]
    url = r.url
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))