# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simon_says_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='sequence',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
