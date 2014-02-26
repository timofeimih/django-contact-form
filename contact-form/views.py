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

@ensure_csrf_cookie
def contactview(request):
	subject = u"Заказ от ".encode('utf8') + request.POST.get('name', '').encode('utf8')
	message = request.POST.get('message', '').encode('utf8') + u'<br/>Город: '.encode('utf8') + request.POST.get('town', '').encode('utf8') + u'<br/>Телефон: '.encode('utf8') + request.POST.get('phone', '').encode('utf8')
	from_email = request.POST.get('email', '').encode('utf8')

	message = message.encode('utf8')
	subject = subject.encode('utf8')

	if subject and message and from_email:
	        try:
				send_mail(subject, message, from_email, ['timofeimih@gmail.com'])
    		except BadHeaderError:
        			return HttpResponse('Invalid header found.')
    		return HttpResponse("1")
	else:
		return HttpResponse(from_email)

	return HttpResponse(subject)
