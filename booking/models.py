from django.db import models


class Master(models.Model):
    SERVICES = (
        ('B', 'Barber'),
        ('S', 'Stylist'),
        ('C', 'Cosmetologist')
    )
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    service = models.CharField(max_length=1, choices=SERVICES)

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.get_full_name
