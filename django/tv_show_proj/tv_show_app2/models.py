from django.db import models
from datetime import date, datetime
import re

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self,postData):
        # current date and time
        now = date.today()
        datee= datetime.strptime(str(now), "%Y-%m-%d")
        timestamp2 = datetime.timestamp(datee)
        errors={}
        if len(postData['title'])<3:
            errors['title']='Show titel should be at least two character!'
        shows_title=Show.objects.filter(title=postData['title'])
        print(shows_title)
        if shows_title:
            errors['title']='This title is already exist!'
        if len(postData['desc'])<11 and len(postData['desc'])>0:
            errors['desc']='Show description should be at least 10 character!'
        if len(postData['select_network'])<4:
            errors['select_network']='Show network should be at least 10 character!'
        show_date=postData['date']
        date2= datetime.strptime(show_date, "%Y-%m-%d")
        timestamp = datetime.timestamp(date2)
        print(timestamp)
        if timestamp>=timestamp2:
            errors['date']='Show date should be in the past!'
        return errors
    def another(self, postData):
        errors={}
        for i in range(2):
            shows_title2=Show.objects.filter(title=postData['title_edit'])
            if shows_title2 and i==1:
                errors['title_edit']='This title is already exist!'
        return errors

class Network(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=ShowManager()
class Show(models.Model):
    title=models.CharField(max_length=255)
    release_date=models.DateField()
    network=models.ForeignKey(Network,related_name="shows",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    desc=models.TextField()
    objects=ShowManager()
