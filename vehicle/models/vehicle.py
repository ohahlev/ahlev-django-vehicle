from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ..models.maker import Maker
from ..models.vehicle_model import VehicleModel
from ..models.vehicle_color import VehicleColor
from ..models.vehicle_grade import VehicleGrade
from ..models.drive_type import DriveType
from ..models.body_type import BodyType
from ..models.fuel_type import FuelType
from tag.models import Tag

class Vehicle(models.Model):
    
    frame_no = models.CharField(max_length=64, unique=True, verbose_name='Frame No')
    manufacturing_date = models.DateTimeField(verbose_name='Manufacturing Date')
    deposit_date = models.DateTimeField(verbose_name='Deposit Date')
    code = models.CharField(max_length=64, unique=True)
    engine = models.IntegerField(validators=[MinValueValidator(0),])
    mileage = models.IntegerField(validators=[MinValueValidator(0),])
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    vehicle_make = models.ForeignKey(Maker, on_delete=models.CASCADE, verbose_name='Maker')
    vehicle_model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE, verbose_name='Vehicle Model')
    vehicle_color = models.ForeignKey(VehicleColor, on_delete=models.CASCADE, verbose_name='Vehicle Color')
    vehicle_grade = models.ForeignKey(VehicleGrade, on_delete=models.CASCADE, verbose_name='Vehicle Grade')
    drive_type = models.ForeignKey(DriveType, on_delete=models.CASCADE, verbose_name='Drive Type')
    body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE, verbose_name='Body Type')
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE, verbose_name='Fuel Type')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Tag')

    class Meta:
        verbose_name = "Vehicle"

    def __str__(self):
        return self.frame_no

    def save(self, force_insert=False, force_update=False):
        self.code = '{}_{}'.format(self.frame_no, '{}{}'.format(
            self.manufacturing_date.year, self.manufacturing_date.month))
        super(Vehicle, self).save(force_insert, force_update)
