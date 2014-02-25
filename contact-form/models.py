########## models.py #############
from django import forms
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError

# A simple contact form with four fields.
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    message = forms.CharField(widget=Textarea())
    town = forms.CharField()