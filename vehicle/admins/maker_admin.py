from django.utils.html import format_html
from django.contrib import admin
from imagekit.admin import AdminThumbnail
from imagekit.cachefiles import ImageCacheFile
from ..models.vehicle import Vehicle
from ..models.maker import Maker

class MakerAdmin(admin.ModelAdmin):

    def preview_thumbnail(self, obj):
        if obj.logo_thumbnail:
            return format_html(u"<img src='{}'/>", obj.logo_thumbnail.url)
    preview_thumbnail.short_description = 'Preview'

    readonly_fields = ['preview_thumbnail']
    
    fieldsets = [
        (None, {
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
        
admin.site.register(Maker, MakerAdmin)