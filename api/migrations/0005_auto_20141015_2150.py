# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_auto_20141015_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneBookLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.BigIntegerField(unique=True)),
                ('member_type', models.CharField(max_length=10, choices=[(b'SD', b'Student'), (b'FA', b'Faculty'), (b'SF', b'Staff')])),
                ('added_on', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=True, help_text=b'Designates if entries are active(True) or deleted(False)')),
                ('added_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(related_name=b'members', to='api.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserDetail',
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
        migrations.RemoveField(
            model_name='phonebook',
            name='added_by',
        ),
        migrations.RemoveField(
            model_name='phonebook',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='head_of',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='privileges',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserDetails',
        ),
        migrations.AlterField(
            model_name='singlemessagelog',
            name='sent_to',
            field=models.ForeignKey(to='api.PhoneBookLog'),
        ),
        migrations.DeleteModel(
            name='PhoneBook',
        ),
    ]
