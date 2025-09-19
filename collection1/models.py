
# collection/models.py
from django.db import models

class Gown(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gowns/')  # Images saved in media/gowns/
    category = models.CharField(max_length=50, choices=[('collection', 'collection'), ('party', 'Party')])
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name

class WeddingVideo(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')  # Videos saved in media/videos/

    def __str__(self):
        return self.title

class MaidsDress(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    image = models.ImageField(upload_to='maids_dresses/')

    def __str__(self):
        return self.name
