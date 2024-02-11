from django.db import models

# Create your models here.


class Test(models.Model):
    my_image = models.ImageField(null =True, blank=True, upload_to='images')
    name = models.CharField(null =True, blank=True, max_length=200)