# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import uuidfield.fields
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageDetails',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('id', uuidfield.fields.UUIDField(primary_key=True, serialize=False, editable=False, max_length=32, blank=True, unique=True)),
                ('sent_on', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(default=b'single', max_length=20, verbose_name='Message Type', choices=[(b'group', b'Group'), (b'single', b'Single')])),
                ('request_id', models.CharField(max_length=255, verbose_name='Single/Group Message ID')),
                ('sent_to', models.CharField(max_length=255, verbose_name='Single/Group ID')),
                ('number_list', models.TextField(default=None, null=True, verbose_name='Numbers list', blank=True)),
                ('provider', models.CharField(default=b'BhashSMS', max_length=20, verbose_name='SMS Service Provider', choices=[(b'BhashSMS', b'BhashSMS')])),
                ('message_ids', models.TextField(default=None, null=True, verbose_name='SMS API Message IDs', blank=True)),
                ('sent', models.BooleanField(default=False, verbose_name='Delivery Status')),
                ('status_list', models.TextField(default=None, null=True, verbose_name='Message Delivery Status', blank=True)),
                ('response_code', models.CharField(default=None, max_length=100, null=True, verbose_name='SMS API Response code', blank=True)),
                ('sent_by', models.ForeignKey(related_name=b'sms_messagedetails_sent', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
