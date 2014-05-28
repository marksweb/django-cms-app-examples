# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Clinic'
        db.create_table('injury_clinics', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tier', self.gf('django.db.models.fields.IntegerField')(max_length=1)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('specialism', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('logo', self.gf('imageuploader.fields.model.ImageField')()),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('town', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('clicks', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal(u'clinics', ['Clinic'])


    def backwards(self, orm):
        # Deleting model 'Clinic'
        db.delete_table('injury_clinics')


    models = {
        u'clinics.clinic': {
            'Meta': {'object_name': 'Clinic', 'db_table': "'injury_clinics'"},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'clicks': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('imageuploader.fields.model.ImageField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'specialism': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tier': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['clinics']