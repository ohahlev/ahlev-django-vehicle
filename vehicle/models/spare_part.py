from django.db import models
from tinymce.models import HTMLField
from tag.models import Tag

class SparePart(models.Model):
    name = models.CharField(max_length=32, unique=True)
    detail = HTMLField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Tag')

    class Meta:
        verbose_name = 'Spare Part'
        db_table = 'spare_part'

    def __str__(self):
        return self.name
