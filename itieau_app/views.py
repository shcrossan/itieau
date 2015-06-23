

__author__ = 'shanecrossan'

#django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

#local
from forms import AddContactForm
from models import contact

#Lib
import requests

@login_required()
def home(request):
    url = '/' + request.user.username + '/'
    return HttpResponseRedirect(url)

@login_required()
def addContact(request):
    contact_list = contact.objects.filter(user=request.user)
    form = AddContactForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.user = request.user
        save_it.save()
        return HttpResponseRedirect('')

    return render_to_response('contact.html', locals(), context_instance=RequestContext(request))

@login_required()
def deleteContact(request, id):
    contact_del = contact.objects.filter(user=request.user).get(id=id)
    contact_del.delete()
    return redirect('/contact/')

def editContact(request, id):
    contact_edit = contact.objects.filter(user=request.user).get(id=id)
    form = AddContactForm(request.POST or None, instance=contact_edit)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.user = request.user
        save_it.save()
        return redirect('/contact/')
    return render_to_response('contact.html', locals(), context_instance=RequestContext(request))

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

    r4 = requests.get("http://107.170.192.206/teapiri2.php")
    text4 = r4.text.encode('ASCII', 'ignore')
    split_text4 = str.split(text4, 'Bornier local')
    value4 = split_text4[5][-5:]
    value_str4 = str.strip(value4, '\x1e')
    value_round4 = round(float(value_str4))

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

    r5 = requests.get("http://107.170.192.206/tavararo.php")
    text5 = r5.text.encode('ASCII', 'ignore')
    split_text5 = str.split(text5, 'Bornier')
    value5 = split_text5[6][-5:]
    value_str5 = str.strip(value5, '\x1e')
    value_round5 = round(float(value_str5))

    r6 = requests.get("http://107.170.192.206/vaitea.php")
    text6 = r6.text.encode('ASCII', 'ignore')
    split_text6 = str.split(text6, 'Bornier local')
    value6 = split_text6[5][-5:]
    value_str6 = str.strip(value6, '\x1e')
    value_round6 = round(float(value_str6))

    r7 = requests.get("http://107.170.192.206/cowan.php")
    text7 = r7.text.encode('ASCII', 'ignore')
    split_text7 = str.split(text7, 'Bornier')
    value7 = split_text7[6][-5:]
    value_str7 = str.strip(value7, '\x1e')
    value_round7 = round(float(value_str7))

    r8 = requests.get("http://107.170.192.206/oscar.php")
    text8 = r8.text.encode('ASCII', 'ignore')
    split_text8 = str.split(text8, 'Bornier')
    value8 = split_text8[3][-5:]
    value_str8 = str.strip(value8, '\x1e')
    value_round8 = round(float(value_str8))

    r9 = requests.get("http://107.170.192.206/passard.php")
    text9 = r9.text.encode('ASCII', 'ignore')
    split_text9 = str.split(text9, 'Bornier')
    value9 = split_text9[5][-5:]
    value_str9 = str.strip(value9, '\x1e')
    value_round9 = round(float(value_str9))

    r10 = requests.get("http://107.170.192.206/passard.php")
    text10 = r10.text.encode('ASCII', 'ignore')
    split_text10 = str.split(text10, 'Bornier')
    value10 = split_text10[5][-5:]
    value_str10 = str.strip(value10, '\x1e')
    value_round10 = round(float(value_str10))

    r11 = requests.get("http://107.170.192.206/puurai1.php")
    text11 = r11.text.encode('ASCII', 'ignore')
    split_text11 = str.split(text11, 'Bornier')
    value11 = split_text11[5][-5:]
    value_str11 = str.strip(value11, '\x1e')
    value_round11 = round(float(value_str11))

    r12 = requests.get("http://107.170.192.206/puurai2.php")
    text12 = r12.text.encode('ASCII', 'ignore')
    split_text12 = str.split(text12, 'Bornier')
    value12 = split_text12[5][-5:]
    value_str12 = str.strip(value12, '\x1e')
    value_round12 = round(float(value_str12))

    r13 = requests.get("http://107.170.192.206/puurai3.php")
    text13 = r13.text.encode('ASCII', 'ignore')
    split_text13 = str.split(text13, 'Bornier')
    value13 = split_text13[0][-5:]
    value_str13 = str.strip(value13, '\x1e')
    value_round13 = round(float(value_str13))

    return render_to_response('marie/faaa.html', locals(), context_instance=RequestContext(request))


def demo(request):
    if request.user.username != 'demo':
        return HttpResponseRedirect('/')
    value = 0.90
    value_round = round(value)

    value2 = 2.93
    value_round2 = round(value2)

    value3 = 5.12
    value_round3 = round(value3)

    return render_to_response('marie/demo.html', locals(), context_instance=RequestContext(request))