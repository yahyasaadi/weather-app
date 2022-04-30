from django.db import models

# Create your models here.
class City(models.Model):

    city_name = models.CharField(max_length=40)
    continent = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.city_name