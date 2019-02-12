from django.http import HttpResponse
from django.shortcuts import render

from booking.models import Master


def index(request):
    masters_list = Master.objects.order_by('-id')
    return render(request, 'booking/index.html', {'masters': masters_list})


def detail(request, master_id):
    master = Master.objects.get(id=master_id)
    return HttpResponse(f"Master {master.get_full_name} is a {master.get_service_display()}")
