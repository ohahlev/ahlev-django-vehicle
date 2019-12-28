from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

class Maker(models.Model):
    name = models.CharField(max_length=32, unique=True)
    logo = models.ImageField(upload_to='maker')
    logo_thumbnail = ImageSpecField(source='logo', 
        processors=[ResizeToFit(None, 200)],
        format='PNG',
        options={'quality': 100})
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Maker"

    def __str__(self):
        return self.name