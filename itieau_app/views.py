__author__ = 'shanecrossan'

#django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

#local
from forms import AddContactForm
from models import contact, Url

#Lib
import requests

@login_required()
def home(request):
    url = Url.objects.filter(user=request.user).order_by('position')
    count = 0
    url_list = []
    for url_obj in url:
        r = requests.get("http://107.170.192.206/" + url_obj.script)
        text = r.text.encode('ASCII', 'ignore')
        split_text = str.split(text, 'Bornier')
        value = split_text[url_obj.bornierSpilt][-5:]
        value_str = str.strip(value, '\x1e')
        value_round = round(float(value_str))
        url_list.append([url_obj.name, url_obj.position, value, value_round])

    return render_to_response('home.html', locals(), context_instance=RequestContext(request))

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

@login_required()
def waterLevels(request):
    url = Url.objects.filter(user=request.user).order_by('position')
    count = 0
    url_list = []
    for url_obj in url:
        r = requests.get("http://107.170.192.206/"+url_obj.script)
        text = r.text.encode('ASCII', 'ignore')
        split_text = str.split(text, 'Bornier')
        value = split_text[url_obj.bornierSpilt][-5:]
        value_str = str.strip(value, '\x1e')
        value_round = round(float(value_str))
        url_list.append([url_obj.name, url_obj.position, value, value_round ])

    return render_to_response('home.html', locals(), context_instance=RequestContext(request))
