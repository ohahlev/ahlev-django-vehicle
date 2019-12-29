from django.db import models
from ..models.vehicle import Vehicle
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

class VehiclePhoto(models.Model):
    photo = models.ImageField(upload_to='photo')
    photo_thumbnail = ImageSpecField(source='photo', 
        processors=[ResizeToFit(None, 200)],
        format='PNG',
        options={'quality': 100})
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Vehicle')
    
    class Meta:
        verbose_name = 'Vehicle Photo'
        db_table = 'vehicle_photo'

