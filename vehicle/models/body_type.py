from django.db import models


class BodyType(models.Model):
    name = models.CharField(max_length=32, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Body Type'
        db_table = 'body_type'

    def __str__(self):  
        return self.name


