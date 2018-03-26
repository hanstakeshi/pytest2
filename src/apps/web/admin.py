# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin

from filebrowser.settings import ADMIN_THUMBNAIL
from apps.core.actions import export_as_csv_action
from singlemodeladmin import SingleModelAdmin
from models import (Home, HomeBanner, Banners, InfoSite, Contacto, )


# tinymce
STATIC_URL = settings.STATIC_URL
# js_tiny = [
#     '{0}grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js'.format(STATIC_URL),
#     '{0}grappelli/tinymce_setup/tinymce_setup.js'.format(STATIC_URL),
# ]

admin_css = {"all": ("css/geoposition.css",)}


class InfoSiteAdmin(SingleModelAdmin):
    fieldsets = (
        ('', {'fields': ('direccion', 'email', 'telefono',
                         'email_form', 'paquetes', 'foto_contactanos')}),
        ('Social', {'fields': ('facebook',
                               'twitter', 'linkedin', 'skype', 'intranet')}),
        ('Site/SEO', {'fields': ('site', 'ga', 'coordenadas')})
    )

    class Media:
        css = admin_css

    def has_add_permission(self, request):
        info = InfoSite.objects.all()
        if info:
            return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        return False


class HomeBannerInline(admin.StackedInline):
    model = HomeBanner
    extra = 0
    ordering = ['position']


class HomeAdmin(SingleModelAdmin):
    model = Home
    fieldsets = (
        ('Nuestro Diferencial', {
            'fields': ('texto_diferencial', 'imagen_diferencial', 'fondo_diferencial')}),
        (u'Equipo', {
            'fields': ('imagen_equipo',)}),
        ('Video', {
            'fields': ('imagen_video', 'video_enlace')}),
        )
    inlines = [HomeBannerInline]

    def has_add_permission(self, request):
        home = Home.objects.all()
        if home:
            return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        return False


class BannersAdmin(admin.ModelAdmin):
    model = Banners

    # def has_add_permission(self, request):
    #     banner = Banners.objects.all()
    #     if banner:
    #         return False
    #     else:
    #         return True

    # def has_delete_permission(self, request, obj=None):
    #     return False


class ContactoAdmin(admin.ModelAdmin):
    model = Contacto
    list_display = ('nombre', 'email', 'fecha', 'tipo', 'telefono')
    readonly_fields = ('nombre', 'email', 'fecha', 'tipo',
                       'telefono', 'mensaje')
    search_fields = ['nombre', 'email', 'tipo']
    ordering = ['-fecha']
    list_filter = ['fecha', 'tipo']
    list_per_page = 25
    actions = [export_as_csv_action()]


admin.site.register(InfoSite, InfoSiteAdmin)
admin.site.register(Home, HomeAdmin)
admin.site.register(Banners, BannersAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.unregister(Group)
admin.site.unregister(Site)
