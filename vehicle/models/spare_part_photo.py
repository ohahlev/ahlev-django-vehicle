from django.db import models
from ..models.spare_part import SparePart
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

class SparePartPhoto(models.Model):
    photo = models.ImageField(upload_to='spare_part_photo')
    photo_thumbnail = ImageSpecField(source='photo', 
        processors=[ResizeToFit(None, 200)],
        format='PNG',
        options={'quality': 100})
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    spare_part = models.ForeignKey(SparePart, on_delete=models.CASCADE, verbose_name='Spare Part')

    class Meta:
        verbose_name = "Spare Part Photo"

