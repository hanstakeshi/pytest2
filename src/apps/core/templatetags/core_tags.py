# -*- coding: utf-8 -*-

from logging import getLogger
import re

from django import template
from django.template.defaultfilters import safe, stringfilter
from django.utils.numberformat import format
from ..util.youtube import YoutubeVideo

log = getLogger('django')


register = template.Library()


@register.filter
@stringfilter
def br(text):
    '''
        Convierte dos barras inclinadas en un salto de línea
    '''

    text = text.replace('//', '<br>')
    return safe(text)


@register.filter
def floatdot(value, decimal_pos=4):
    '''
        Similar a floatformat, pero utiliza punto en vez de la coma
    '''
    value = str(value).replace(',', '.')
    return format(value, ".", decimal_pos)

floatdot.is_safe = True


@register.filter
def get_range(value):
    '''
        Idéntico a xrange
    '''

    return xrange(value)


@register.filter
def get_item(dictionary, key):
    '''
        Obtiene un item del diccionario por nombre de atributo
    '''

    return dictionary.get(key, '')


@register.filter
def split(string, char='//'):
    '''
        Idéntico a split
    '''

    return string.split(char)


@register.filter
def tel(txt):
    ''' Extrae los caracteres númericos de un teléfono '''
    lista = re.findall('\d+', txt)
    telefono = ''.join(lista)
    return telefono


@register.filter
@stringfilter
def youtube_embed(url):
    '''
        Genera la url para incrustar videos de Youtube en base a la url normal.
    '''
    yv = YoutubeVideo(url)
    return yv.embed_url


@register.filter
@stringfilter
def youtube_img(url, size):
    '''
        Genera la url de la iamgen miniatura de un video en youtube en base a
        la url normal y su tamaño.
    '''
    yv = YoutubeVideo(url)
    return yv.get_img(size)


@register.filter
@stringfilter
def youtube_id(url):
    '''
        Genera la url para incrustar videos de Youtube en base a la url normal.
    '''
    yv = YoutubeVideo(url)
    return yv.id
