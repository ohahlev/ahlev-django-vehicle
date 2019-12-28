from django.db import models
from tinymce.models import HTMLField

class SparePart(models.Model):
    name = models.CharField(max_length=32, unique=True)
    detail = HTMLField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Spare Part"

    def __str__(self):
        return self.name