from django.db import models

# Create your models here.

class ImageUploader(models.Model):
    photo = models.ImageField(upload_to='img/',null=True,blank=True)
    date = models.DateTimeField(auto_now_add = True)