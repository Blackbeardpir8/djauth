from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import UserManager
# Create your models here

class CustomUser(AbstractUser):
    username = None
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12, unique=True)
    parofile_image = models.ImageField(upload_to="profile",null=True,blank=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'

    REQUIRED_FIELDS = ['name',]

    objects = UserManager()