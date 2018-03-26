# -*- coding: utf-8 -*-

# IMPORTS
# from datetime import date
from logging import getLogger
from urlparse import urlparse

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models
from ckeditor.fields import RichTextField

from apps.core.models import AuditableModel, SlugModel, PositionModel
from geoposition.fields import GeopositionField
from filebrowser.fields import FileBrowseField

log = getLogger('django')


class Post(models.Model):
    mensaje = models.TextField()

    def __unicode__(self):
        return u"Post"


class ModelExample(models.Model):

    img_example = FileBrowseField('Imagen Label',
                                max_length=200, blank=True,
                                extensions=['.jpg', '.png', '.gif'],
                                directory='img_example')

    rich_example = RichTextField("Example", blank=True)

    class Meta:
        verbose_name = "Model Exmaple"
        verbose_name_plural = "Model Examples"

    def __unicode__(self):
        return u"Model Example"


class InfoSite(AuditableModel):
    direccion = models.CharField('Dirección', max_length=120,
        help_text='Agregar // para generar el salto de línea')
    email = models.EmailField('Email')
    telefono = models.CharField('Teléfono', max_length=60)
    email_form = models.EmailField('Formulario de Contacto', blank=True)
    site = models.CharField("URL del sitio", max_length=60, blank=True,
        help_text='Ingrese la url actual del sitio sin el slash final')

    facebook = models.URLField('Facebook', blank=True)
    twitter = models.URLField('Twitter', blank=True)
    linkedin = models.URLField('Linkedin', blank=True)
    skype = models.CharField('Skype', blank=True, max_length=160)
    intranet = models.URLField('Intranet', blank=True)

    ga = models.CharField('Google Analytics', max_length=24, blank=True,
       help_text='''Opcional: Inserte el código que google analitycs le
       proporciona con el formato: UA-XXXXX-X''')
    coordenadas = GeopositionField()
    paquetes = FileBrowseField("PDF de paquetes", max_length=200,
        directory='paquetes/', extensions=['.doc', '.pdf'], blank=True)
    foto_contactanos = FileBrowseField('Foto de contáctanos', max_length=200,
        directory='contactanos/', extensions=['.jpg', '.png', '.gif'],
        help_text=u'Tamaño recomendado:366x210', blank=True)

    def __unicode__(self):
        return u'Información del Sitio'

    def direccion_local(self):
        texto = self.direccion.replace('//', '')
        return texto

    class Meta:
        verbose_name_plural = u'Información del Sitio'

    def save(self, *args, **kwargs):
        site = Site.objects.get(id=settings.SITE_ID)
        site.domain = urlparse(self.site).netloc
        site.name = settings.PROJECT_NAME
        site.save()

        super(InfoSite, self).save(*args, **kwargs)


# HOME
class Home(models.Model):
    # NUESTRO DIFERENCIAL
    texto_diferencial = RichTextField('Texto')
    imagen_diferencial = FileBrowseField('Imagen', max_length=200,
        directory='home/', extensions=['.jpg', '.png', '.gif'], blank=True)
    fondo_diferencial = FileBrowseField('Fondo', max_length=200,
        directory='home/', extensions=['.jpg', '.png', '.gif'], blank=True)
    # EQUIPO
    imagen_equipo = FileBrowseField('Imagen de equipo', max_length=200,
        directory='home/', extensions=['.jpg', '.png', '.gif'], blank=True)
    # VIDEO
    imagen_video = FileBrowseField("Imagen Video", max_length=200,
        directory='home/', extensions=['.jpg', '.png', '.gif'], blank=True)
    video_enlace = models.URLField('URL del Video', blank=True)

    class Meta:
        verbose_name = u'Home'
        verbose_name_plural = u'Home'

    def __unicode__(self):
        return u'Home'


class HomeBanner(PositionModel):
    home = models.ForeignKey(Home, related_name='banners_home')
    titulo = models.CharField("Titulo:", max_length=100)
    subtitulo = models.CharField("Subtítulo", max_length=100, blank=True)
    texto_1 = models.CharField("Texto 1", max_length=100, blank=True)
    texto_2 = models.CharField("Texto 2", max_length=100, blank=True)
    conocenos_texto = models.CharField("Texto de botón",
                                       null=True, blank=True, max_length=100)
    enlace_boton = models.URLField('Enlace del botón', blank=True)
    fondo = FileBrowseField('Fondo:', max_length=200,
                            directory='home_banners/',
                            extensions=['.jpg', '.png', '.gif'], blank=True,
                            help_text='Tamaño Recomendado: 1920x400')
    pdf = FileBrowseField("PDF", max_length=200,
                          directory='home/', extensions=['.pdf'], blank=True)

    class Meta:
        verbose_name = u'Banner de Home'
        verbose_name_plural = u'Banners de Home'
        ordering = ['position']

    def __unicode__(self):
        return unicode(self.titulo)
# ENDHOME


# BANNERS
class Banners(models.Model):
    CHOICES = (
        ('S', 'SOMOS'),
        ('SE', 'SERVICIOS'),
        ('E', 'EQUIPO'),
        ('T', 'TESTIMONIOS'),
        ('C', u'CONTÁCTANOS'),
    )
    pestana = models.CharField("Pestaña",
                               max_length=30, choices=CHOICES, default='S')
    titulo = models.CharField("Título", max_length=200)
    texto = RichTextField('Texto')
    imagen = FileBrowseField('Imagen:', max_length=200,
                             directory='banners/',
                             extensions=['.jpg', '.png', '.gif'],
                             help_text='Tamaño Recomendado: 1919X279')

    class Meta:
        verbose_name = u'Banners'
        verbose_name_plural = u'Banners'
        # ordering = ['position']

    def __unicode__(self):
        return self.titulo


# FORMULARIOS
class Contacto(models.Model):
    fecha = models.DateTimeField('Fecha', auto_now_add=True)
    tipo = models.CharField('Tipo de cliente', max_length=120)
    nombre = models.CharField('Nombre', max_length=120)
    email = models.EmailField('Email')
    telefono = models.CharField("Telefono", max_length=80)
    # empresa = models.CharField("Empresa", max_length=100)
    mensaje = models.TextField('Mensaje')

    class Meta:
        verbose_name = u'Contacto'
        verbose_name_plural = u'Contactos'
        ordering = ['-fecha']

    def __unicode__(self):
        return u'{0}: {1}'.format(self.email, self.fecha.date())
