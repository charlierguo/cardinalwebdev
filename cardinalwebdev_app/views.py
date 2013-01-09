from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.core.validators import email_re
from django.http import HttpResponse, HttpResponseRedirect
from coffin.shortcuts import render_to_response, get_object_or_404, render, \
    redirect
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_exempt

from cardinalwebdev_app.models import *
from cardinalwebdev_app.model_forms import *
from cardinalwebdev_app.forms import *

try:
    import json
except ImportError:
    import simplejson as json

def index(request):
    application = ApplyForm()
    if request.method == "POST":
        application = ApplyForm(request.POST)
        if application.is_valid():
            cd = application.cleaned_data
            app = Application(
                name=cd['name'],
                email=cd['email'],
                attendance=cd['attendance'],
                interest=cd['interest'],
                background=cd['background'],
                comments=cd['comments'])
            app.save()
            msg = 'Thanks for applying! If you wanna chat, email \
                <a href="mailto:kevin@imkevinxu.com?Subject=Cardinal%20Web%20Dev%20Chat" \
                target="_blank">kevin@imkevinxu.com</a>'
            status = 'success'
            return HttpResponse(json.dumps({'msg' : msg,'status' : status }, ensure_ascii=False), mimetype='application/json')
        else:
            return render(request, "contactus.html", locals())

    return render(request, "index.html", locals())

# Helper Functions
def is_valid_email(email):
    return True if email_re.match(email) else False

def email(request):
    msg = 'Sorry there was a slight error, please try again.'
    status = 'error'
    if request.is_ajax() and 'email' in request.POST:
        if is_valid_email(request.POST['email']):
            e, created = Email.objects.get_or_create(email=request.POST['email'])
            status = 'success'
            if created:
                e.save()
                msg = 'Thanks for contacting us! We\'ll be in touch soon.'
            else:
                msg = 'Thanks! If you wanna chat, email <a href="mailto:kevin@imkevinxu.com?Subject=Cardinal%20Web%20Dev%20Chat" target="_blank">kevin@imkevinxu.com</a>'
        else:
            msg = 'Sorry email address looks odd, please try again.'

    return HttpResponse(json.dumps({
        'msg' : msg,
        'status' : status
        }, ensure_ascii=False), mimetype='application/json')


