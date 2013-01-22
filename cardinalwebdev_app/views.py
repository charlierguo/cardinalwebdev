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

import operator

try:
    import json
except ImportError:
    import simplejson as json

def index(request):
    return render(request, "index.html", locals())

# -----------------------------------------
#   APPLICATION FUNCTIONS
# -----------------------------------------

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
            appreview = ApplicationReview(application=app)
            appreview.save()
            results = json.dumps({ 'status' : 'success' }, ensure_ascii=False)
            return HttpResponse(results, mimetype='application/json')
        return render(request, "application.html", locals())
    return redirect('index')

def review(request):
    if not request.user.is_superuser:
        return redirect('index')
    apps = sorted(ApplicationReview.objects.all(), key=operator.attrgetter('application.created_at'))
    return render(request, "review.html", locals())

def submit_review(request):
    if request.is_ajax() and request.method == "POST":
        app_id = int(request.POST['application'])
        editor = request.POST['editor']
        decision = int(request.POST['decision'])
        comments = request.POST['comments']
        review = ApplicationReview.objects.get(id=app_id)
        if editor == 'charlie':
            review.charlie_decision = decision
            review.charlie_comments = comments
        elif editor == 'kevin':
            review.kevin_decision = decision
            review.kevin_comments = comments
        elif editor == 'kingston':
            review.kingston_decision = decision
            review.kingston_comments = comments
        review.save()
        results = json.dumps({ 'decision' : decision, 'total' : review.total }, ensure_ascii=False)
        return HttpResponse(results, mimetype='application/json')
    return redirect('review')

# -----------------------------------------
#   STUDENT FUNCTIONS
# -----------------------------------------

def students(request):
    students = Student.objects.all()
    return render(request, "students.html", locals())

def lecture(request, lecture_id):
    return render(request, "lectures/lecture%s.html" % lecture_id, locals())