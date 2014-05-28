# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tracking'
        db.create_table('charity_listings_tracking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('listing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['listings.Listing'])),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('clicks', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'listings', ['Tracking'])


    def backwards(self, orm):
        # Deleting model 'Tracking'
        db.delete_table('charity_listings_tracking')


    models = {
        u'listings.listing': {
            'Meta': {'object_name': 'Listing', 'db_table': "'charity_listings'"},
            'category': ('django.db.models.fields.IntegerField', [], {}),
            'charity_desc': ('django.db.models.fields.TextField', [], {}),
            'charity_image': ('imageuploader.fields.model.ImageField', [], {}),
            'charity_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'charity_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'clicks': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'tier': ('django.db.models.fields.IntegerField', [], {'max_length': '1'})
        },
        u'listings.tracking': {
            'Meta': {'object_name': 'Tracking', 'db_table': "'charity_listings_tracking'"},
            'clicks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listing': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['listings.Listing']"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['listings']