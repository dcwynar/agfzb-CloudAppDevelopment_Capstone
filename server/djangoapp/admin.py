from django.contrib import admin
from .models import CarMake, CarModel

# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    model = CarModel

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    model = CarMake
    inlines = [CarModelInline]

admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)
