from django.db import models


class Yoga(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)
    benifit = models.TextField(max_length=5000)
    gif  = models.FileField(upload_to="yoga_gifs/")
    dis = models.CharField(max_length=255,default='default_value')



