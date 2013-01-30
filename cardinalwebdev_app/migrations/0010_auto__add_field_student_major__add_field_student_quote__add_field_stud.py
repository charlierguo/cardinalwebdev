# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Student.major'
        db.add_column('cardinalwebdev_app_student', 'major',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Student.quote'
        db.add_column('cardinalwebdev_app_student', 'quote',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Student.twitter'
        db.add_column('cardinalwebdev_app_student', 'twitter',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Student.github'
        db.add_column('cardinalwebdev_app_student', 'github',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Student.facebook'
        db.add_column('cardinalwebdev_app_student', 'facebook',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Student.major'
        db.delete_column('cardinalwebdev_app_student', 'major')

        # Deleting field 'Student.quote'
        db.delete_column('cardinalwebdev_app_student', 'quote')

        # Deleting field 'Student.twitter'
        db.delete_column('cardinalwebdev_app_student', 'twitter')

        # Deleting field 'Student.github'
        db.delete_column('cardinalwebdev_app_student', 'github')

        # Deleting field 'Student.facebook'
        db.delete_column('cardinalwebdev_app_student', 'facebook')


    models = {
        'cardinalwebdev_app.application': {
            'Meta': {'object_name': 'Application'},
            'attendance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'background': ('django.db.models.fields.TextField', [], {}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest': ('django.db.models.fields.TextField', [], {}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'cardinalwebdev_app.applicationreview': {
            'Meta': {'object_name': 'ApplicationReview'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cardinalwebdev_app.Application']"}),
            'charlie_comments': ('django.db.models.fields.TextField', [], {}),
            'charlie_decision': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kevin_comments': ('django.db.models.fields.TextField', [], {}),
            'kevin_decision': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'kingston_comments': ('django.db.models.fields.TextField', [], {}),
            'kingston_decision': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        'cardinalwebdev_app.student': {
            'Meta': {'object_name': 'Student'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'github': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'quote': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['cardinalwebdev_app']