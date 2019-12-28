from django.utils.html import format_html
from django.contrib import admin
from imagekit import ImageSpec
from imagekit.admin import AdminThumbnail
from imagekit.processors import ResizeToFill
from imagekit.cachefiles import ImageCacheFile
from ..models.vehicle_model import VehicleModel
from .widgets import AdminSmallestThumbnailSpec, AdminSmallThumbnailSpec

class VehicleModelAdmin(admin.ModelAdmin):

    def preview_thumbnail(self, obj):
        if obj.logo_thumbnail:
            return format_html(u"<img src='{}'/>", obj.logo_thumbnail.url)
    preview_thumbnail.short_description = 'Preview'

    readonly_fields = ['preview_thumbnail']
    
    fieldsets = [
        ("NAME", {
            'fields': ['name', 'logo', 'preview_thumbnail'],
        }),
    ]
    search_fields = ['name']
    list_display = ['name', 'preview_thumbnail', 'date_created', 'last_updated']

    class Media:
        css = {
        'all': (
            'vehicle/css/vehicle.css',
            )
         }
        '''
        js = (
            'js/jquery.min.js', 
            'js/popper.min.js',
            'js/bootstrap.min.js',
            'js/mdb.min.js',
            'js/myscript.js'
        )
        '''

admin.site.register(VehicleModel, VehicleModelAdmin)