from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(
        default='profile_pictures/default_image.jpg',
        upload_to='profile_pictures')
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username