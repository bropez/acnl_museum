from django.db import models


class Fish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.CharField(max_length=255)
    price = models.IntegerField()
    shadow = models.CharField(max_length=255, default='small')
    location = models.CharField(max_length=255, default='river')
    months_available = models.CharField(max_length=255, default='All year')
    time = models.CharField(max_length=255, default='all day')

    def __str__(self):
        return self.name
