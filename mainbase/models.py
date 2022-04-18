from django.db import models
from bathrooms.models import BathRoom
from hometypes.models import HomeTypes
from metro.models import Metro
from balcons.models import Balcon
from owners.models import Owner


class MainBase(models.Model):
    type = models.ForeignKey(HomeTypes, on_delete=models.CASCADE, null=True)
    numbers_flat = models.IntegerField()
    price = models.IntegerField()
    square_meters = models.IntegerField()
    address = models.CharField(max_length=255)
    metro = models.ForeignKey(Metro, on_delete=models.CASCADE, null=True)
    bath_room = models.ForeignKey(BathRoom, on_delete=models.CASCADE, null=True)
    balcon = models.ForeignKey(Balcon, on_delete=models.CASCADE, null=True)
    holders = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
        

    def __str__(self):
        return self.address



    