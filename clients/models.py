from django.db import models
from django.utils import timezone
from django import forms


import datetime
class Client(models.Model):
    name=models.CharField(max_length=50)
    number_id=models.IntegerField()
    email= models.EmailField(max_length=50)
    born_date=models.DateField(verbose_name='Born date')
    create_date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
        return self.born_date.strftime('%Y/%m/%d')
    
    