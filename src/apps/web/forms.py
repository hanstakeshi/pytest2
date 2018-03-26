# -*- coding: utf-8 -*-
from logging import getLogger

from django.forms import ModelForm
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage
from django.conf import settings


from .models import (Contacto)
from .util import get_info


log = getLogger('django')


class ContactoForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(ContactoForm, self).__init__(*args, **kwargs)

        # custom widget attribute:
        # self.fields['asunto'].widget.attrs["placeholder"] = 'asunto'

    class Meta:
        model = Contacto
        fields = ('tipo', 'nombre', 'email', 'telefono', 'mensaje')

    def enviaEmail(self):
        htmly = get_template('web/email-contacto.html')
        info = get_info()
        c_d = self.cleaned_data
        c_d['info'] = info
        c_d['SITE'] = info.site
        c_d['STATIC_URL'] = c_d['SITE'] + '/' + settings.STATIC_URL
        d = Context(c_d)
        html_content = htmly.render(d)
        asunto = u'Nukleo: Contacto'
        mail = 'Nukleo<{}>'.format(settings.DEFAULT_FROM_EMAIL)
        emails_destino = info.email_form.split(',')
        msg = EmailMessage(asunto, html_content, mail, emails_destino)
        msg.content_subtype = "html"
        msg.send()
