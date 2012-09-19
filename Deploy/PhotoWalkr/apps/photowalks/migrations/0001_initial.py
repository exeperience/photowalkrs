# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'PhotoWalkStats'
        db.create_table('photowalks_photowalkstats', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('likes', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('views', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('num_participants', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('photowalks', ['PhotoWalkStats'])

        # Adding M2M table for field liked_by on 'PhotoWalkStats'
        db.create_table('photowalks_photowalkstats_liked_by', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photowalkstats', models.ForeignKey(orm['photowalks.photowalkstats'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('photowalks_photowalkstats_liked_by', ['photowalkstats_id', 'user_id'])

        # Adding model 'PhotoWalk'
        db.create_table('photowalks_photowalk', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photos.Photo'], null=True, blank=True)),
            ('admin', self.gf('django.db.models.fields.related.ForeignKey')(related_name='as_suggestion_pw', to=orm['auth.User'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.GroupProfile'], null=True, blank=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photos.Album'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('location', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tags', self.gf('tagging.fields.TagField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 8, 4, 12, 30, 45))),
            ('stats', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photowalks.PhotoWalkStats'], null=True, blank=True)),
        ))
        db.send_create_signal('photowalks', ['PhotoWalk'])

        # Adding M2M table for field participants on 'PhotoWalk'
        db.create_table('photowalks_photowalk_participants', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photowalk', models.ForeignKey(orm['photowalks.photowalk'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('photowalks_photowalk_participants', ['photowalk_id', 'user_id'])


    def backwards(self, orm):
        
        # Deleting model 'PhotoWalkStats'
        db.delete_table('photowalks_photowalkstats')

        # Removing M2M table for field liked_by on 'PhotoWalkStats'
        db.delete_table('photowalks_photowalkstats_liked_by')

        # Deleting model 'PhotoWalk'
        db.delete_table('photowalks_photowalk')

        # Removing M2M table for field participants on 'PhotoWalk'
        db.delete_table('photowalks_photowalk_participants')


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
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'photos.album': {
            'Meta': {'object_name': 'Album'},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.GroupProfile']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_photowalk_album': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['photos.Photo']", 'null': 'True', 'blank': 'True'}),
            'privacy': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'photos.photo': {
            'Meta': {'object_name': 'Photo'},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.PhotoInfo']", 'null': 'True', 'blank': 'True'}),
            'notification_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'privacy': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'stats': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Stats']", 'null': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'photos.photoinfo': {
            'Meta': {'object_name': 'PhotoInfo'},
            'aperture': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'camera': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'focallength': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'shutterspeed': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'taken': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 5, 25, 3, 6, 48, 249081)', 'null': 'True', 'blank': 'True'})
        },
        'photos.stats': {
            'Meta': {'object_name': 'Stats'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_photowalks': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'liked_by': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'photowalks.photowalk': {
            'Meta': {'object_name': 'PhotoWalk'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'as_suggestion_pw'", 'to': "orm['auth.User']"}),
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Album']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 8, 4, 12, 30, 45)'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.GroupProfile']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Photo']", 'null': 'True', 'blank': 'True'}),
            'stats': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photowalks.PhotoWalkStats']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tags': ('tagging.fields.TagField', [], {})
        },
        'photowalks.photowalkstats': {
            'Meta': {'object_name': 'PhotoWalkStats'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liked_by': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'num_participants': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'profiles.groupprofile': {
            'Meta': {'object_name': 'GroupProfile'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'as_group_admin'", 'to': "orm['auth.User']"}),
            'display_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'location_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'as_member'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'photowalk_suggestions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'as_suggestion'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['photowalks.PhotoWalk']"}),
            'stats': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['profiles.GroupStats']", 'null': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {})
        },
        'profiles.groupstats': {
            'Meta': {'object_name': 'GroupStats'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liked_by': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'num_members': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'num_photos': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'num_photowalks': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        }
    }

    complete_apps = ['photowalks']
