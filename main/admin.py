from django.contrib import admin
from .models import Address, Event, HouseholdItem
# Register your models here.

admin.site.register(Address)
admin.site.register(Event)
admin.site.register(HouseholdItem)