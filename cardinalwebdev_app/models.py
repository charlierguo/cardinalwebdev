from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django import forms

import datetime
import os

class Base(models.Model):
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True, auto_now=True)

    class Meta:
        abstract = True

class Application(Base):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    major = models.CharField(max_length=255)
    attendance = models.BooleanField()
    interest = models.TextField()
    background = models.TextField()
    comments = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u'%s\'s Application' % (self.name)