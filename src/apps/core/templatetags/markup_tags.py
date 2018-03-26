# -*- coding: utf-8 -*-

from logging import getLogger

from django import template
from django.template.defaultfilters import stringfilter

log = getLogger('django')

try:
    from markdown import markdown
except ImportError:
    log.warning('markdown missing!')
    MARKDOWN = False
else:
    MARKDOWN = True

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def mrkdwn(txt):
    '''
        Convierte un texto en markdown a html de manera "segura"
    '''
    if MARKDOWN:
        return markdown(txt, safe_mode='remove', output_format='html5',
            enable_attributes=False)
    else:
        return txt
