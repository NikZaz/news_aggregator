from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import User



class News(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    image_url = models.URLField(blank=True)
    full_text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

