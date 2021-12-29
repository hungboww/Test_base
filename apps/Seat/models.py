from django.db import models

# Create your models here.
from apps.Staff.models import UserModel


class FloorModel(models.TextChoices):
    Tang11 = '11'
    Tang13 = 'Tầng 13'
    Tang15 = 'Tầng 15'
    Tang17 = 'Tầng 17'


class SeatModel(models.Model):
    Floor = [
        ('11', 'T11'),
        ('13', 'T13'),
        ('15', 'T15'),
        ('17', 'T17'),
    ]
    id_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='seatmodel')
    status = models.CharField(max_length=5)
    position = models.CharField(max_length=10)
    floor = models.CharField(max_length=20, choices=Floor, default='11')

    class Meta:
        indexes = [models.Index(fields=['floor'])]
