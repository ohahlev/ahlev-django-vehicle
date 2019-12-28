from django.utils.html import format_html
from django.contrib import admin
from ..models.body_type import BodyType


class BodyTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['name'],
        }),
    ]
    list_display = ('name', 'date_created', 'last_updated')
    search_fields = ['name']

admin.site.register(BodyType, BodyTypeAdmin)