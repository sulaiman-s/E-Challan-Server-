from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)


class ProfilePic(models.Model):
    name = models.CharField(max_length=255)
    profile_img = models.ImageField(upload_to='profiles', blank=False)
