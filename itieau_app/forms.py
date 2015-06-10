__author__ = 'shanecrossan'

#django
from django import forms

#local
from models import *

class AddContactForm(forms.ModelForm):
    class Meta:
        model = contact
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(AddContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['position'].widget.attrs.update({'class': 'form-control'})
        self.fields['number'].widget.attrs.update({'class': 'form-control'})