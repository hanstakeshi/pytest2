# -*- coding: utf-8 -*-

from logging import getLogger

from .models import InfoSite

log = getLogger('django')


def get_info():
    """ Obtiene o crea una instancia de InfoSite en caso de que no exista """
    info, created = InfoSite.objects.get_or_create(pk=1, defaults={
        'email_form': 'desarrollo@email.com',
        'telefono': '051-47852365',
        'direccion': 'Calle 28 de julio San isidro',
        'facebook': 'http://facebook.com/',
        'site': 'http://127.0.0.1:8000',
    })

    return info
