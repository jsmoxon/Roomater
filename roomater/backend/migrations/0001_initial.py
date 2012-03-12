# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'UserProfile'
        db.create_table('backend_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('clean_score', self.gf('django.db.models.fields.IntegerField')()),
            ('food_score', self.gf('django.db.models.fields.IntegerField')()),
            ('about', self.gf('django.db.models.fields.TextField')()),
            ('pic', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('backend', ['UserProfile'])

        # Adding model 'Question'
        db.create_table('backend_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('questioner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('backend', ['Question'])

        # Adding model 'Response'
        db.create_table('backend_response', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('responder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Question'])),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('backend', ['Response'])

        # Adding model 'Survey'
        db.create_table('backend_survey', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('backend', ['Survey'])

        # Adding M2M table for field questions on 'Survey'
        db.create_table('backend_survey_questions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('survey', models.ForeignKey(orm['backend.survey'], null=False)),
            ('question', models.ForeignKey(orm['backend.question'], null=False))
        ))
        db.create_unique('backend_survey_questions', ['survey_id', 'question_id'])

        # Adding model 'ResponseList'
        db.create_table('backend_responselist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Survey'])),
        ))
        db.send_create_signal('backend', ['ResponseList'])

        # Adding M2M table for field responses on 'ResponseList'
        db.create_table('backend_responselist_responses', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('responselist', models.ForeignKey(orm['backend.responselist'], null=False)),
            ('response', models.ForeignKey(orm['backend.response'], null=False))
        ))
        db.create_unique('backend_responselist_responses', ['responselist_id', 'response_id'])


    def backwards(self, orm):
        
        # Deleting model 'UserProfile'
        db.delete_table('backend_userprofile')

        # Deleting model 'Question'
        db.delete_table('backend_question')

        # Deleting model 'Response'
        db.delete_table('backend_response')

        # Deleting model 'Survey'
        db.delete_table('backend_survey')

        # Removing M2M table for field questions on 'Survey'
        db.delete_table('backend_survey_questions')

        # Deleting model 'ResponseList'
        db.delete_table('backend_responselist')

        # Removing M2M table for field responses on 'ResponseList'
        db.delete_table('backend_responselist_responses')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'backend.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'questioner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'backend.response': {
            'Meta': {'object_name': 'Response'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backend.Question']"}),
            'responder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'backend.responselist': {
            'Meta': {'object_name': 'ResponseList'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'responses': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['backend.Response']", 'symmetrical': 'False'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backend.Survey']"})
        },
        'backend.survey': {
            'Meta': {'object_name': 'Survey'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'questions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['backend.Question']", 'symmetrical': 'False'})
        },
        'backend.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'clean_score': ('django.db.models.fields.IntegerField', [], {}),
            'food_score': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['backend']
