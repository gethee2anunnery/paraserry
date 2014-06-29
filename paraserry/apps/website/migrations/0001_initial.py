# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'website_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project_title', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('launch_date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('main_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('about', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('images', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'website', ['Project'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'website_project')


    models = {
        u'website.project': {
            'Meta': {'object_name': 'Project'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'launch_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'main_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'project_title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['website']