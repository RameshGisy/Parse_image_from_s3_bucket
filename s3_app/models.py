from django.db import models

# Create your models here.
class Farmer_image(models.Model):
    image_name = models.CharField(max_length=500,null=True)
    date_time = models.CharField(max_length=500,null=True)