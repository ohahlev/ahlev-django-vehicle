from django.db import models


class VehicleColor(models.Model):
    name = models.CharField(max_length=32, unique=True)
    code = models.CharField(max_length=32, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Vehicle Color"
        verbose_name_plural = "Vehicle Colors"

    def __str__(self):  
        return self.name


