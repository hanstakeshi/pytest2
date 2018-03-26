from django.contrib import admin
from .models import SEO


class SEOAdmin(admin.ModelAdmin):
    list_display = ('url', 'meta_title')
    list_per_page = 25
    search_fields = ('url', 'meta_title')

admin.site.register(SEO, SEOAdmin)
