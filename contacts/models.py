from django.db import models
from datetime import datetime

# Create your models here.

class Contact(models.Model):
    user_id = models.IntegerField(blank=True)
    car_id = models.IntegerField()
    price = models.IntegerField(default=0)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    customer_need = models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.first_name
