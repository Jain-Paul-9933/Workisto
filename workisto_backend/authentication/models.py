from django.db import models
from django.contrib.auth.models import AbstractUser
from service.models import ServiceLocation,Services,ServiceTime

class CustomUser(AbstractUser):

    email=models.EmailField(max_length=50,unique=True)
    phone_number=models.CharField(max_length=50)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['phone_number','username']

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    dob=models.DateField(null=True)
    address_lane_1=models.CharField(max_length=300)
    address_lane_2=models.CharField(max_length=300)
    pincode=models.CharField(max_length=50)
    profile_photo=models.ImageField(upload_to='user/profile_photo')

    def __str__(self):
        return self.user.username
    
    
class WorkerProfile(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    address_lane_1 = models.CharField(max_length=300)
    address_lane_2 = models.CharField(max_length=300)
    pincode = models.CharField(max_length=50)
    profile_photo = models.ImageField(upload_to='worker/profile_photo')
    qualification_name = models.CharField(max_length=100, null=True)
    qualification_doc = models.FileField(upload_to="worker/qualification_doc", null=True)
    certification_name = models.CharField(max_length=100, null=True)
    certification_doc = models.FileField(upload_to="worker/certification_doc", null=True)
    license_name = models.CharField(max_length=100, null=True)
    license_doc = models.FileField(upload_to="worker/license_doc", null=True)
    experience = models.IntegerField(null=True)
    health_insurance_name = models.CharField(max_length=100, null=True)
    health_insurance_doc = models.FileField(upload_to="worker/health_insurance_doc", null=True)
    preferred_location = models.OneToOneField(ServiceLocation, on_delete=models.CASCADE, null=True)
    emergency_service = models.BooleanField(default=False)
    services_providing = models.ManyToManyField(Services)
    service_time = models.OneToOneField(ServiceTime, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username