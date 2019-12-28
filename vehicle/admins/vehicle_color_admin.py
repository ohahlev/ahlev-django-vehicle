from django.utils.html import format_html
from django.contrib import admin
from ..models.vehicle_color import VehicleColor


class VehicleColorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['name', 'code'],
        }),
    ]
    list_display = ('name', 'code', 'date_created', 'last_updated')
    search_fields = ['name']

admin.site.register(VehicleColor, VehicleColorAdmin)