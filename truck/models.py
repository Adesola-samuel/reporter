from django.db import models

class UpperCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(UpperCharField, self).__init__(*args, **kwargs)
    
    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname, None)
        if value:
            value = value.upper()
            value = value.replace(' ', '-')
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(Selection, self).pre_save(model_instance, add)
        
# Create your models here.
class Truck(models.Model):
    cab_no = UpperCharField(max_length=14)
    truck_no = models.CharField(max_length=14, null=True, blank=True)
    officer = models.CharField(max_length=25, null=True, blank=True)
    fleet = models.CharField(max_length=14, null=True, blank=True)
    
    def __str__(self):
        return f"{self.cab_no} : {self.officer} : {self.fleet}"


class Selection(models.Model):
    cab_no = UpperCharField(max_length=14)
    officer = models.CharField(max_length=25, null=True, blank=True)
    date = models.DateField(auto_now_add =True)
    fleet = models.CharField(max_length=14, null=True, blank=True)

    def __str__(self):
        return f"{self.cab_no} {self.officer}"
    

class Exit(models.Model):
    cab_no = UpperCharField(max_length=14)
    officer = models.CharField(max_length=25, null=True, blank=True)
    fleet = models.CharField(max_length=14, null=True, blank=True)
    date = models.DateField(auto_now_add =True)

    def __str__(self):
        return f"{self.cab_no} {self.officer} {self.date}"
    
class Admmission(models.Model):
    cab_no = UpperCharField(max_length=14)
    officer = models.CharField(max_length=25, null=True, blank=True)
    fleet = models.CharField(max_length=14, null=True, blank=True)
    date = models.DateField(auto_now_add =True)

    def __str__(self):
        return f"{self.cab_no} {self.officer} {self.date} {self.fleet}"