from django.views import generic

from booking.models import Master


class MastersList(generic.ListView):
    model = Master
    template_name = 'booking/index.html'


class MasterDetails(generic.DetailView):
    model = Master
    template_name = 'booking/master.html'
