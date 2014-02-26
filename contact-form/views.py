########## views.py ##############
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from models import ContactForm
from django.template import RequestContext, Context
from django import forms
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError
from django.views.decorators.csrf import ensure_csrf_cookie
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import quopri
def QuoHead(String):
    s = quopri.encodestring(String.encode('UTF-8'), 1, 0)
    return "=?utf-8?Q?" + s.decode('UTF-8') + "?="
@ensure_csrf_cookie
def contactview(request):
	subject =QuoHead("Заказ от " + request.POST.get('name', ''))
	message = QuoHead(request.POST.get('message', '') + u'<br/>Город: ' + request.POST.get('town', '') + u'<br/>Телефон: ' + request.POST.get('phone', ''))
	from_email = request.POST.get('email', '')

	message = MIMEText(message.encode('utf-8'), 'plain', 'UTF-8')
	subject	= MIMEText(subject.encode('utf-8'), 'plain', 'UTF-8')

	if subject and message and from_email:
	        try:
				send_mail(subject, message, from_email, ['timofeimih@gmail.com'])
    		except BadHeaderError:
        			return HttpResponse('Invalid header found.')
    		return HttpResponse("1")
	else:
		return HttpResponse(from_email)

	return HttpResponse(subject)
