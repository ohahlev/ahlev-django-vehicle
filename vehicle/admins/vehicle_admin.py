
from django.contrib import admin
from ..models.vehicle import Vehicle
from ..models.vehicle_make import VehicleMake
from django.utils.html import format_html
from ..models.photo import Photo
from django.db import models

class PhotoInline(admin.StackedInline):
    '''
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget},
    }
    '''
    def preview_thumbnail(self, obj):
        if obj.photo_thumbnail:
            return format_html(u"<img src='{}'/>", obj.photo_thumbnail.url)
    preview_thumbnail.short_description = 'Preview'

    readonly_fields = ['preview_thumbnail']
    fieldsets = [
        (None, {
            'fields': ['image', 'preview_thumbnail'],
        }),
    ]
    model = Photo
    extra = 1

class VehicleAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    fieldsets = [
        ('BASIC', {
            'fields': [
                'frame_no', 'engine', 'mileage'
            ],
        }),
        ('DATE', {
            'fields': [
                'manufacturing_date', 'deposit_date'
            ],
        }),
        ('MORE', {
            'fields': [
                'vehicle_make', 'vehicle_model', 'vehicle_color', 'vehicle_grade', 
                'drive_type', 'body_type', 'fuel_type'
            ],
        })
    ]
    list_display = ['frame_no', 'preview_thumbnail', 'date_created', 'last_updated', 'engine', 'mileage', 
        'manufacturing_date', 'deposit_date', 'vehicle_make', 'vehicle_model', 'vehicle_color', 
        'vehicle_grade', 'drive_type', 'body_type', 'fuel_type']

    search_fields = ['frame_no', 'engine', 'mileage', 'vehicle_make__name', 'vehicle_model__name', 
        'vehicle_color__name', 'vehicle_grade__name', 'drive_type__name', 'body_type__name', 
        'fuel_type__name']

    def save_model(self, request, obj, form, change):
        obj.save()
        for afile in request.FILES.getlist('photos_multiple'):
            obj.photo_set.create(image=afile)
    
    def preview_thumbnail(self, obj):
        if obj.photo_set.all():
            return format_html(u"<img src='{}'/>", obj.photo_set.all()[0].photo_thumbnail.url)
    preview_thumbnail.short_description = 'Preview'

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