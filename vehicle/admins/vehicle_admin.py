
from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from ..models.vehicle import Vehicle
from ..models.vehicle_photo import VehiclePhoto

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
    model = VehiclePhoto
    extra = 1

class VehicleAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    fieldsets = [
        ('BASIC', {
            'fields': ['frame_no', 'engine', 'mileage'],
        }),
        ('DATE', {
            'fields': ['manufacturing_date', 'deposit_date'],
        }),
        ('CODE', {
            'fields': ['code']
        }),
        ('MORE', {
            'fields': [
                'tag', 'vehicle_make', 'vehicle_model', 'vehicle_color', 'vehicle_grade', 
                'drive_type', 'body_type', 'fuel_type'
            ],
        })
    ]
    list_display = ['code', 'preview_tag', 'frame_no', 'preview_thumbnail', 'date_created', 'last_updated', 'engine', 'mileage', 
        'manufacturing_date', 'deposit_date', 'vehicle_make', 'vehicle_model', 'vehicle_color', 
        'vehicle_grade', 'drive_type', 'body_type', 'fuel_type']

    search_fields = ['frame_no', 'code', 'engine', 'mileage', 'vehicle_make__name', 'vehicle_model__name', 
        'vehicle_color__name', 'vehicle_grade__name', 'drive_type__name', 'body_type__name', 
        'fuel_type__name']

    readonly_fields = ['code']

    def save_model(self, request, obj, form, change):
        obj.save()
        for afile in request.FILES.getlist('photos_multiple'):
            obj.vehiclephoto_set.create(photo=afile)
    
    def preview_thumbnail(self, obj):
        if obj.vehiclephoto_set.all():
            return format_html(u"<img src='{}'/>", obj.vehiclephoto_set.all()[0].photo_thumbnail.url)
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

admin.site.register(Vehicle, VehicleAdmin)