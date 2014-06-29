# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field tags on 'Project'
        m2m_table_name = db.shorten_name(u'website_project_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'website.project'], null=False)),
            ('tag', models.ForeignKey(orm[u'website.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'tag_id'])


    def backwards(self, orm):
        # Removing M2M table for field tags on 'Project'
        db.delete_table(db.shorten_name(u'website_project_tags'))


    models = {
        u'website.project': {
            'Meta': {'object_name': 'Project'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'launch_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'main_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'project_title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'project_tags'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['website.Tag']"}),
            'txtid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'website.tag': {
            'Meta': {'ordering': "['title']", 'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['website.Tag']", 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['website']