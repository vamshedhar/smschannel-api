# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagedetails',
            name='message',
            field=models.TextField(default=None, null=True, verbose_name='Message Content', blank=True),
            preserve_default=True,
        ),
    ]
