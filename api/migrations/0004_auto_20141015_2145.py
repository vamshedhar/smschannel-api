# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_auto_20141015_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMessageLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sent_on', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('delivery_status', models.IntegerField(max_length=1, choices=[(1, b'Success'), (0, b'Failure')])),
                ('sent_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('sent_to', models.ForeignKey(to='api.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SingleMessageLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sent_on', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('delivery_status', models.IntegerField(max_length=1, choices=[(1, b'Success'), (0, b'Failure')])),
                ('sent_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('sent_to', models.ForeignKey(to='api.PhoneBook')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('head_of', models.ForeignKey(related_name=b'head', to='api.Group', null=True)),
                ('privileges', models.ManyToManyField(related_name=b'privileged_members', null=True, to='api.Group')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='phonebook',
            name='active',
            field=models.BooleanField(default=True, help_text=b'Designates if entries are active(True) or deleted(False)'),
            preserve_default=True,
        ),
    ]
