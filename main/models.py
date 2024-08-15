from django.db import models

# Create your models here.
class Address(models.Model):
    address = models.CharField('Address', max_length = 100)

    def __str__(self):
        return self.address

class Event(models.Model):
    DAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
    ]
    
    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.get_day_display()}: {self.start_time} - {self.end_time}"
    
class HouseholdItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField('Image')

    def __str__(self):
        return self.name    