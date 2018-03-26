from .models import (InfoSite)


def web_processor(request):
    """ Variables globales """
    info, created = InfoSite.objects.get_or_create(pk=1)

    return locals()
