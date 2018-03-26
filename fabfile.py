#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps
from site import addsitedir
from os.path import abspath, dirname, join
import json
import sys

from fabric.api import local, task, env
from fabric.colors import blue, green
from fabric.context_managers import prefix
from fabric.contrib import django

from fab_extras import cron

# Añadimos la raiz del proyecto al path
BASE_DIR = abspath(join(dirname(__file__), 'src'))
sys.path.append(BASE_DIR)

with open(join(BASE_DIR, 'settings/settings.json')) as f:
    ENV = json.load(f)

# Añadimos virtualenv al path
WORKON_HOME = ENV['WORKON_HOME']
DJANGO_ENV = ENV['ENV']
addsitedir('{0}/{1}/lib/python2.7/site-packages'.format(WORKON_HOME, DJANGO_ENV))


django.settings_module('settings')

env.shell = '/bin/bash'

# from django.conf import settings


# VIRTUALENV
def virtualenv():
    '''
        Context manager. Usado para ejecutar acciones con virtualenv activado::

        with virtualenv():
            # virtualenv está activo aquí
    '''

    return prefix('export ENV="{0}";. {1}/{0}/bin/activate'.format(DJANGO_ENV, WORKON_HOME))


def inside_virtualenv(func):
    '''
        Decorador, usado para ejecutar acciones con virtualenv activado::

        @task
        @inside_virtualenv
        def my_command():
            # virtualenv está activo aquí
    '''
    @wraps(func)
    def inner(*args, **kwargs):
        with virtualenv():
            return func(*args, **kwargs)
    return inner


# TAREAS
@task
@inside_virtualenv
def cache(extra=''):
    ''' Activa el backend para la cache '''
    if extra == 'dev':
        print(blue(':: cache ::'))
        local('./src/manage.py createcachetable cache_table')
        print(green('::: cache() :::'))
    else:
        print(blue(':: memcached ::'))
        local('mkdir -p ~/scripts')
        local('cp extra/memcached_usage.sh ~/scripts/memcached_usage.sh')
        cron_line = '*/5 * * * * cd ~/scripts;./memcached_usage.sh > /dev/null 2>&1'
        cron.update_line(cron_line, 'memcached')
        print(green('::: memcached() :::'))


@task
@inside_virtualenv
def migrate():
    ''' Ejecuta las migraciones '''
    print(blue(':: migrate ::'))
    local('./src/manage.py migrate --settings=settings.production')
    print(green('::: migrate() :::'))


@task
@inside_virtualenv
def commit(descript='mensaje', user='usuario'):
    ''' Ejecuta las migraciones '''
    print(blue(':: addremove ::'))
    local("hg addremove")

    print(blue(':: commit ::'))
    local("hg commit -u '{0}' -m '{1}'".format(descript, user))

    print(blue(':: pull -u ::'))
    local("hg pull -u")

    print(blue('::push ::'))
    local("hg push")

    print(green('::: Cambios subidos con exito :::'))


@task
@inside_virtualenv
def pep8():
    ''' validación pep8. '''
    print(blue(':: pep8() ::'))
    local('pep8 --config setup.cfg .')
    print(green('::: pep8() :::'))


@task
@inside_virtualenv
def static():
    ''' Ejecuta el comando collectstatic '''
    print(blue(':: static() ::'))

    local('./src/manage.py collectstatic --noinput --settings=settings.production')

    print(green('::: static() :::'))


@task
def stylus():
    ''' Compila código stylus. '''
    print(blue(':: stylus() ::'))

    local('stylus -w src/static/styl/ -o src/static/css/')

    print(green('::: stylus() :::'))


@task
@inside_virtualenv
def test(extra=''):
    ''' Ejecuta los test's '''
    print(blue(':: test() ::'))

    if extra == 'dev':
        local('./src/manage.py test --settings=settings.dev')
        pep8()
    else:
        local('./src/manage.py test')
    print(green('::: test() :::'))
