

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