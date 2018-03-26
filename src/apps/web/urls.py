# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

app_name = 'web'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contactanos/$', views.contactanos, name='contactanos'),
    url(r'^gracias/$', views.gracias, name='gracias'),

    # API

    # AJAX
    # url(r'^contacto/tipoproducto/$', views.tipoproducto, name='tipoproducto'),
]
