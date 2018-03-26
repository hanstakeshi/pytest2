# coding: utf-8
#
# Código extraido y modificado desde: django-fab-deploy
#

from fabric.api import task, settings, hide, local, puts

__all__ = ['set_content', 'add_line', 'puts_content', 'remove_line',
           'update_line', 'get_content']

sentinel = object()


def _marker(marker):
    return ' # MARKER:%s' % marker if marker is not sentinel else ''


@task
def get_content(hide_stdout=False):
    if hide_stdout:
        _hide = hide('warnings', 'stdout')
    else:
        _hide = hide('warnings')

    with settings(_hide, warn_only=True):
        # local no es capaz de capturar y mostrar salida al mismo tiempo
        local('crontab -l')
        output = local('crontab -l', capture=True)
        return output if output.succeeded else ''


@task
def set_content(content):
    """ Sets crontab content """
    local("echo \"%s\"|crontab -" % content)


@task
def puts_content():
    """ Shows current crontab """
    puts(get_content(hide_stdout=True))


@task
def add_line(content, marker=sentinel):
    """ Adds line to crontab. Line can be appended with special marker
    comment so it'll be possible to reliably remove or update it later. """
    old_crontab = get_content(hide_stdout=True)
    marker = _marker(marker)
    set_content(old_crontab + '\n' + content + marker)
    return marker


@task
def remove_line(marker):
    """ Removes a line added and marked using add_line. """
    marker = _marker(marker)
    lines = [line for line in get_content(hide_stdout=True).splitlines()
             if line and not line.endswith(marker)]
    set_content("\n".join(lines))


@task
def update_line(content, marker):
    """ Adds or updates a line in crontab. """
    remove_line(marker)
    return add_line(content, marker)
