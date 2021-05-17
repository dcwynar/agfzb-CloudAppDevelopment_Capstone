from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=127)
    description = models.CharField(max_length=511)
    def __str__(self):
        return '<CarMake: ' + self.name + '>'

class CarModel(models.Model):
    id = models.AutoField(primary_key=True)
    make = ForeignKey(CarMake, on_delete=CASCADE)
    name = models.CharField(max_length=127)
    dealer_id = models.PositiveIntegerField()
    type = models.CharField(max_length=31, choices=(
        ('suv', 'SUV'), 
        ('sedan', 'Sedan'),
        ('wagon', 'WAGON'),
        ('coupe', 'Coupe'),
        ('hatchback', 'Hatchback'),
        ('compact', 'Compact')
    ))
    year = models.DateField()
    def __str__(self):
        return '<CarModel: ' + self.make.name + ': ' + self.name + '>'


class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        self.address = address
        self.city = city
        self.full_name = full_name
        self.id = id
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.st = st
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name


# <HINT> Create a plain Python class `DealerReview` to hold review data
