from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking/<int:master_id>', views.detail, name='detail'),
]
