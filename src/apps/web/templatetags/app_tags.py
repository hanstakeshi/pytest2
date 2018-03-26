# -*- coding: utf-8 -*-

import re

from django import template
from apps.web.util import get_info

register = template.Library()


# HEADER
@register.inclusion_tag('common/_header.html')
def header():
    info = get_info()

    return locals()


# FOOTER
@register.inclusion_tag('common/_footer.html')
def footer():
    info = get_info()

    return locals()


@register.filter
def tel(txt):
    """ Extrae los caracteres númericos de un teléfono """
    lista = re.findall('\d+', txt)
    telefono = ''.join(lista)
    return telefono
