from django.db import models

class Balcon(models.Model):
    balcon_type = models.CharField(max_length=100)

    def __str__(self):
        return self.balcon_type
