from django.contrib import admin
from .models import Redirect


class RedirectAdmin(admin.ModelAdmin):
    list_display = ('old_path', 'new_path')
    list_per_page = 25
    search_fields = ('old_path', 'new_path')

admin.site.register(Redirect, RedirectAdmin)
