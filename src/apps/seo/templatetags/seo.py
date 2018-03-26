# -*- coding: utf-8 -*-

from django import template
from ..models import SEO

register = template.Library()


@register.inclusion_tag('seo/metatags.html', takes_context=True)
def metatags(context):
    path = context['request'].path
    title = context.get('meta_title')
    description = context.get('meta_description')

    try:
        seo_object = SEO.objects.get(url=path)
        title = seo_object.meta_title
        description = seo_object.meta_description
    except SEO.DoesNotExist:
        pass

    return {
        'title': title,
        'description': description
    }
