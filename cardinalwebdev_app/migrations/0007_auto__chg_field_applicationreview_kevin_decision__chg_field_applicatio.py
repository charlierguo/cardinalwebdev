# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ApplicationReview.kevin_decision'
        db.alter_column('cardinalwebdev_app_applicationreview', 'kevin_decision', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'ApplicationReview.charlie_decision'
        db.alter_column('cardinalwebdev_app_applicationreview', 'charlie_decision', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'ApplicationReview.kingston_decision'
        db.alter_column('cardinalwebdev_app_applicationreview', 'kingston_decision', self.gf('django.db.models.fields.IntegerField')())

    def backwards(self, orm):

        # Changing field 'ApplicationReview.kevin_decision'
        db.alter_column('cardinalwebdev_app_applicationreview', 'kevin_decision', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ApplicationReview.charlie_decision'
        db.alter_column('cardinalwebdev_app_applicationreview', 'charlie_decision', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'ApplicationReview.kingston_decision'
        db.alter_column('cardinalwebdev_app_applicationreview', 'kingston_decision', self.gf('django.db.models.fields.PositiveIntegerField')())

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
        }
    }

    complete_apps = ['cardinalwebdev_app']