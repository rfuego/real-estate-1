from django.db import models

class Owner(models.Model):
    holder = models.CharField(max_length=100)

    def __str__(self):
        return self.holder
