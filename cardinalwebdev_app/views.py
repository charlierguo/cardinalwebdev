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
    return render(request, "index.html", locals())

def apply(request):
    if request.is_ajax() and request.method == "POST":
        application = ApplyForm(request.POST)
        if application.is_valid():
            cd = application.cleaned_data
            app = Application(
                  name=cd['name'],
                  email=cd['email'],
                  major=cd['major'],
                  attendance=cd['attendance'],
                  interest=cd['interest'],
                  background=cd['background'],
                  comments=cd['comments'])
            app.save()
            results = json.dumps({ 'status' : 'success' }, ensure_ascii=False)
            return HttpResponse(results, mimetype='application/json')
        return render(request, "application.html", locals())
    return redirect('index')