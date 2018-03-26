# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seo',
            name='meta_description',
            field=models.CharField(help_text=b'M\xc3\xa1ximo 160 caracteres', max_length=160, verbose_name=b'Descripci\xc3\xb3n', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='seo',
            name='meta_title',
            field=models.CharField(help_text=b'M\xc3\xa1ximo: 50 caracteres', max_length=50, verbose_name=b'T\xc3\xadtulo', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='seo',
            name='url',
            field=models.CharField(help_text=b'Debe ingresar la url relativa. Por ejemplo: "/contacto/"', unique=True, max_length=200, verbose_name=b'URL', db_index=True),
            preserve_default=True,
        ),
    ]
