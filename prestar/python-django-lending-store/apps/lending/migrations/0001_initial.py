# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prestario',
            fields=[
                ('id_prestario', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.TextField(max_length=20)),
                ('apellido', models.TextField(max_length=20)),
                ('DNI', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='prestador',
            fields=[
                ('id_prestador', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.TextField(max_length=20)),
                ('apellido', models.TextField(max_length=20)),
                ('DNI', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='objeto',
            fields=[
                ('id_objeto', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(null=True)),
                ('id_prestario', models.ForeignKey(to='objeto.prestario')),
                ('id_prestador', models.ForeignKey(to='objeto.prestador')),
            ],
        ),
    ]
