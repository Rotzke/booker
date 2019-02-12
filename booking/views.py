from django.http import HttpResponse
from django.shortcuts import render

from booking.models import Master


def index(request):
    masters_list = Master.objects.order_by('-id')
    output = '<br>'.join([f'<a href="{q.id}">{q.get_full_name}</a>' for q in masters_list])
    return HttpResponse(output)


def detail(request, master_id):
    master = Master.objects.get(id=master_id)
    return HttpResponse(f"Master {master.get_full_name} is a {master.get_service_display()}")
