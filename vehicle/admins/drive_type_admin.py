from django.utils.html import format_html
from django.contrib import admin
from ..models.drive_type import DriveType


class DriveTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['name'],
        }),
    ]
    list_display = ('name', 'date_created', 'last_updated')
    search_fields = ['name']

admin.site.register(DriveType, DriveTypeAdmin)