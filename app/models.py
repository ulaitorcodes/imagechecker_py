
from django.db import models

class Image(models.Model):
    image_file = models.ImageField(upload_to='images/')
