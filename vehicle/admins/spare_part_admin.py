from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from ..models.spare_part import SparePart
from ..models.spare_part_photo import SparePartPhoto

class PhotoInline(admin.StackedInline):

    def preview_thumbnail(self, obj):
        if obj.photo_thumbnail:
            return format_html(u"<img src='{}'/>", obj.photo_thumbnail.url)
    preview_thumbnail.short_description = 'Preview'
    readonly_fields = ['preview_thumbnail']
    fieldsets = [
        (None, {
            'fields': ['photo', 'preview_thumbnail'],
        }),
    ]
    model = SparePartPhoto
    extra = 1

class SparePartAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    search_fields = ['name', 'detail', 'tag']
    list_display = ['name', 'preview_tag', 'date_created', 'last_updated', 'preview_detail']
    fieldsets = [
        (None, {
            'fields': ['name', 'tag', 'detail']
        }),
    ]
    def save_model(self, request, obj, form, change):
        obj.save()
        for afile in request.FILES.getlist('photos_multiple'):
            obj.sparepartphoto_set.create(photo=afile)
    
    def preview_detail(self, obj):
        return format_html(obj.detail)
    preview_detail.admin_order_field = 'detail'
    preview_detail.short_description = 'detail'

    def preview_thumbnail(self, obj):
        if obj.sparepartphoto_set.all():
            return format_html(u"<img src='{}'/>", obj.sparepartphoto_set.all()[0].photo_thumbnail.url)
    preview_thumbnail.short_description = 'Preview'

    def preview_tag(self, obj):
        return format_html('<span class="badge badge-pill %s">%s</span>' % (obj.tag.type, obj.tag.name))
    preview_tag.admin_order_field = 'tag'
    preview_tag.short_description = 'preview tag'

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

admin.site.register(SparePart, SparePartAdmin)