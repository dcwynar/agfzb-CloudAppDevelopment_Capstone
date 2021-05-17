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


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
