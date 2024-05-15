from django.db import models


class CarPart(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField()

    def __str__(self):
        return self.name


# Create your models here.
