# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Feed'
        db.create_table('feeds_feed', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('photowalk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photowalks.PhotoWalk'], null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photos.Photo'], null=True, blank=True)),
            ('update_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('feeds', ['Feed'])

        # Adding model 'UserWall'
        db.create_table('feeds_userwall', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('feeds', ['UserWall'])

        # Adding M2M table for field feeds on 'UserWall'
        db.create_table('feeds_userwall_feeds', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userwall', models.ForeignKey(orm['feeds.userwall'], null=False)),
            ('feed', models.ForeignKey(orm['feeds.feed'], null=False))
        ))
        db.create_unique('feeds_userwall_feeds', ['userwall_id', 'feed_id'])

        # Adding model 'Notification'
        db.create_table('feeds_notification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('notification_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User'], null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photos.Photo'], null=True, blank=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.GroupProfile'], null=True, blank=True)),
            ('photowalk', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['photowalks.PhotoWalk'], null=True, blank=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('feeds', ['Notification'])

        # Adding model 'UserNotifications'
        db.create_table('feeds_usernotifications', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('notify', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('feeds', ['UserNotifications'])

        # Adding M2M table for field notifications on 'UserNotifications'
        db.create_table('feeds_usernotifications_notifications', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('usernotifications', models.ForeignKey(orm['feeds.usernotifications'], null=False)),
            ('notification', models.ForeignKey(orm['feeds.notification'], null=False))
        ))
        db.create_unique('feeds_usernotifications_notifications', ['usernotifications_id', 'notification_id'])


    def backwards(self, orm):
        
        # Deleting model 'Feed'
        db.delete_table('feeds_feed')

        # Deleting model 'UserWall'
        db.delete_table('feeds_userwall')

        # Removing M2M table for field feeds on 'UserWall'
        db.delete_table('feeds_userwall_feeds')

        # Deleting model 'Notification'
        db.delete_table('feeds_notification')

        # Deleting model 'UserNotifications'
        db.delete_table('feeds_usernotifications')

        # Removing M2M table for field notifications on 'UserNotifications'
        db.delete_table('feeds_usernotifications_notifications')


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
        'feeds.feed': {
            'Meta': {'object_name': 'Feed'},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'feed_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Photo']", 'null': 'True', 'blank': 'True'}),
            'photowalk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photowalks.PhotoWalk']", 'null': 'True', 'blank': 'True'}),
            'update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'feeds.notification': {
            'Meta': {'object_name': 'Notification'},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.GroupProfile']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notification_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Photo']", 'null': 'True', 'blank': 'True'}),
            'photowalk': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['photowalks.PhotoWalk']", 'null': 'True', 'blank': 'True'}),
            'update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'feeds.usernotifications': {
            'Meta': {'object_name': 'UserNotifications'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notifications': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['feeds.Notification']", 'null': 'True', 'blank': 'True'}),
            'notify': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'feeds.userwall': {
            'Meta': {'object_name': 'UserWall'},
            'feeds': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['feeds.Feed']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
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
            'taken': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 5, 25, 3, 6, 46, 223234)', 'null': 'True', 'blank': 'True'})
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

    complete_apps = ['feeds']
