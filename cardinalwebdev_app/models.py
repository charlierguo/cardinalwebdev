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

class ApplicationReview(Base):
    REVIEW_CHOICES = (
        (0, 'Undecided'),
        (1, 'Accept'),
        (2, 'Reject')
    )
    application = models.ForeignKey(Application)
    charlie_comments = models.TextField()
    charlie_decision = models.PositiveIntegerField(default=0)
    kevin_comments = models.TextField()
    kevin_decision = models.PositiveIntegerField(default=0)
    kingston_comments = models.TextField()
    kingston_decision = models.PositiveIntegerField(default=0)