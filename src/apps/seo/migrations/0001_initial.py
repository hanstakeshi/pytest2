# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SEO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(unique=True, max_length=200, verbose_name=b'URL', db_index=True)),
                ('meta_title', models.CharField(max_length=50, verbose_name=b'T\xc3\xadtulo', blank=True)),
                ('meta_description', models.CharField(max_length=160, verbose_name=b'Descripci\xc3\xb3n', blank=True)),
            ],
            options={
                'ordering': ('url',),
                'verbose_name': 'Metadata',
                'verbose_name_plural': 'Metadata',
            },
            bases=(models.Model,),
        ),
    ]
