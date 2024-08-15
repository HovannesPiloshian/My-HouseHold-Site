from django.shortcuts import render
from .models import Address, Event, HouseholdItem
# Create your views here.
def index(request):
    address_list = Address.objects.all()
    event_list_first = Event.objects.first()  
    event_list_last = Event.objects.last() 
    items_list = HouseholdItem.objects.all()
    return render(request, 'index.html', context = {
        'address_list':address_list,
        'event_list_first': event_list_first,
        'event_list_last': event_list_last,
        'items_list':items_list
    })