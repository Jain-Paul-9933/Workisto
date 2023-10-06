from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    email=models.EmailField(max_length=50,unique=True)
    phone_number=models.CharField(max_length=50)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['phone_number','username']

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    dob=models.DateField()
    address_lane_1=models.CharField(max_length=300)
    address_lane_2=models.CharField(max_length=300)
    pincode=models.CharField(max_length=50)
    profile_photo=models.ImageField(upload_to='article_images/')

    def __str__(self):
        return self.user.username
    