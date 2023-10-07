from django.db import models

class ServiceCategory(models.Model):
    service_category_name=models.CharField(max_length=100)

    def __str__(self):
        return self.service_category_name

class Services(models.Model):
    service_category=models.ForeignKey(ServiceCategory,on_delete=models.CASCADE)
    service_name=models.CharField(max_length=100)

    def __str__(self):
        return self.service_name

class ServiceTime(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name

class ServiceLocation(models.Model):
    location=models.CharField(max_length=100)