# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field documents on 'ContentBlock'
        m2m_table_name = db.shorten_name(u'website_contentblock_documents')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contentblock', models.ForeignKey(orm[u'website.contentblock'], null=False)),
            ('document', models.ForeignKey(orm[u'media.document'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contentblock_id', 'document_id'])


    def backwards(self, orm):
        # Removing M2M table for field documents on 'ContentBlock'
        db.delete_table(db.shorten_name(u'website_contentblock_documents'))


    models = {
        u'media.document': {
            'Meta': {'object_name': 'Document'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['media.Image']", 'null': 'True', 'blank': 'True'}),
            'media_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'media.image': {
            'Meta': {'object_name': 'Image'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'website.contentblock': {
            'Meta': {'object_name': 'ContentBlock'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'documents': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'contentblock_document'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['media.Document']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'contentblock_image'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['media.Image']"}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['website.Project']", 'null': 'True', 'blank': 'True'})
        },
        u'website.project': {
            'Meta': {'object_name': 'Project'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'client': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'launch_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'main_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'project_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'project_tags'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['website.Tag']"}),
            'txtid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'website.resumeitem': {
            'Meta': {'object_name': 'ResumeItem'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'employer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
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