from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


class VehicleModel(models.Model):
    name = models.CharField(max_length=32, unique=True)
    logo = models.ImageField(upload_to='vehicle_model')
    logo_thumbnail = ImageSpecField(source='logo', 
        processors=[ResizeToFit(None, 200)],
        format='PNG',
        options={'quality': 100})
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Vehicle Model"
        verbose_name_plural = "Vehicle Models"

    def __str__(self):  
        return self.name


