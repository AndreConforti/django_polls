import datetime

from django.db import models
from django.utils import timezone

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_register = models.DateTimeField(auto_now_add=timezone.now())
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def was_recently_registered(self):
        return self.date_register >= timezone.now() - datetime.timedelta(days=1)
    
