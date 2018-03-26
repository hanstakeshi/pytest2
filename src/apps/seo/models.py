# -*- coding: utf-8 -*-

from django.db import models


class SEO(models.Model):
    url = models.CharField('URL', max_length=200, db_index=True, unique=True,
        help_text='Debe ingresar la url relativa. Por ejemplo: "/contacto/"')
    meta_title = models.CharField('Título', max_length=50, blank=True,
        help_text='Máximo: 50 caracteres')
    meta_description = models.CharField('Descripción', max_length=160, blank=True,
        help_text='Máximo 160 caracteres')

    class Meta:
        verbose_name = "Metadata"
        verbose_name_plural = "Metadata"
        ordering = ('url',)

    def __unicode__(self):
        return self.url
