# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objeto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower',
            name='needed',
            field=models.IntegerField(null=True),
        ),
    ]
