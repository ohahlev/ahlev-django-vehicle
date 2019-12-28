from django.db import models


class DriveType(models.Model):
    name = models.CharField(max_length=32, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Drive Type"
        verbose_name_plural = "Drive Types"

    def __str__(self):  
        return self.name


