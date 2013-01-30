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
    name       = models.CharField(max_length=255)
    email      = models.EmailField(max_length=254)
    major      = models.CharField(max_length=255)
    attendance = models.BooleanField()
    interest   = models.TextField()
    background = models.TextField()
    comments   = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u'%s\'s Application' % (self.name)

class ApplicationReview(Base):
    application       = models.ForeignKey(Application)
    charlie_comments  = models.TextField()
    charlie_decision  = models.IntegerField(default=0)
    kevin_comments    = models.TextField()
    kevin_decision    = models.IntegerField(default=0)
    kingston_comments = models.TextField()
    kingston_decision = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % (self.application)

    def _total(self):
        return self.charlie_decision + self.kevin_decision + self.kingston_decision

    total = property(_total)

class Student(Base):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=11)

    major = models.CharField(max_length=255, blank=True)
    quote = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    photo = models.URLField(null=True, blank=True)

    # Social Media Usernames
    twitter = models.CharField(max_length=255, blank=True)
    github = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name

    def base_url(self):
        return '/student/%d' % self.id

    def absolute_url(self):
        return '%s/' % self.base_url()