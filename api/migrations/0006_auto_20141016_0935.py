# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_auto_20141015_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPrivileges',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('privileges', models.ManyToManyField(related_name=b'privileged_members', null=True, to='api.Group')),
                ('user', models.ForeignKey(related_name=b'privileges', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='head_of',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='privileges',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserDetail',
        ),
        migrations.AddField(
            model_name='group',
            name='head',
            field=models.ForeignKey(related_name=b'head_of', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
