# -*- coding: utf-8 -*-

from logging import getLogger
# import json

from django.shortcuts import (render_to_response as render, get_object_or_404,
    redirect)
from django.http import JsonResponse
# from django.core.urlresolvers import reverse
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext as ctx
# from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from apps.core.util.util import TextTemplateView
from models import (Home, HomeBanner, Banners, )
from .forms import (ContactoForm,)
from .util import get_info
log = getLogger('django')


# FRONT END
def home(request):
    meta_title = "Nukleo"
    log.info('VIEW: home')
    info = get_info()
    home, created = Home.objects.get_or_create(pk=1)
    home_banners = HomeBanner.objects.filter(
        home_id=home.id).order_by('position')

    return render('web/home.html', locals(), context_instance=ctx(request))


def contactanos(request):
    log.info('VIEW: contacto')
    header = "contactanos"
    meta_title = u"Contáctanos"
    info = get_info()
    banner, created = Banners.objects.get_or_create(pestana='C')

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            if info.email_form:
                form.enviaEmail()
        return redirect('web:gracias')
    else:
        form = ContactoForm()

    return render('web/contacto.html', locals(), context_instance=ctx(request))


def gracias(request):
    log.info('VIEW: home')
    meta_title = "Gracias"
    info = get_info()
    return render('web/gracias.html', locals(), context_instance=ctx(request))


@csrf_exempt
def contacto_asesor(request):
    log.info('VIEW: contacto_asesor')
    data = {'status': 'error'}
    # if request.method == 'POST':
    #     form = ContactoAsesorForm(request.POST)
    #     print form.errors
    #     if form.is_valid():
    #         form.save()
    #         data['status'] = 'ok'

    #     else:
    #         data['msg'] = u'Error de formulario'

    return JsonResponse(data)


class RobotsView(TextTemplateView):
    template_name = "extra/robots.txt"

    def get_context_data(self, **kwargs):
        log.info('VIEW: RobotsView')
        return {'url_base': get_info().site}


def fix_admin(request):
    ''' Redirecciona url's del admin '''
    return redirect(request.path_info + '1/')


def ratelimit_view(request):
    ''' Vista lanzada al activar el bloqueo de django-ratelimit '''
    log.info('VIEW: ratelimit_view')
    info = get_info()

    return render('web/ratelimit.html', locals(), context_instance=ctx(request))


def page_404(request):
    meta_title = u"Página no encontrada"
    ruta = request.path
    log.error('Error 404: {0}'.format(ruta))
    info = get_info()
    response = render('web/error.html', locals(), context_instance=ctx(request))
    response.status_code = 404
    return response


def page_500(request):
    meta_title = u"Página no encontrada"
    ruta = request.path
    log.error('Error 500: {0}'.format(ruta))
    info = get_info()
    response = render('web/error.html', locals(), context_instance=ctx(request))
    response.status_code = 500

    return response
