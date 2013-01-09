# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Email'
        db.delete_table('cardinalwebdev_app_email')


        # Changing field 'Application.interest'
        db.alter_column('cardinalwebdev_app_application', 'interest', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Application.comments'
        db.alter_column('cardinalwebdev_app_application', 'comments', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Application.email'
        db.alter_column('cardinalwebdev_app_application', 'email', self.gf('django.db.models.fields.EmailField')(max_length=254))

        # Changing field 'Application.background'
        db.alter_column('cardinalwebdev_app_application', 'background', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Adding model 'Email'
        db.create_table('cardinalwebdev_app_email', (
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('cardinalwebdev_app', ['Email'])


        # Changing field 'Application.interest'
        db.alter_column('cardinalwebdev_app_application', 'interest', self.gf('django.db.models.fields.CharField')(max_length=1023))

        # Changing field 'Application.comments'
        db.alter_column('cardinalwebdev_app_application', 'comments', self.gf('django.db.models.fields.CharField')(max_length=1023))

        # Changing field 'Application.email'
        db.alter_column('cardinalwebdev_app_application', 'email', self.gf('django.db.models.fields.EmailField')(max_length=255))

        # Changing field 'Application.background'
        db.alter_column('cardinalwebdev_app_application', 'background', self.gf('django.db.models.fields.CharField')(max_length=1023))

    models = {
        'cardinalwebdev_app.application': {
            'Meta': {'object_name': 'Application'},
            'attendance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'background': ('django.db.models.fields.TextField', [], {}),
            'comments': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest': ('django.db.models.fields.TextField', [], {}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cardinalwebdev_app']