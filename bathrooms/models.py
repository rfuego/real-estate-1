from django.db import models

class BathRoom(models.Model):
    bath_room = models.CharField(max_length=100)

    def __str__(self):
        return self.bath_room