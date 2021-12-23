from django.db import models

class Channel(models.Model):
    name = models.CharField(max_length=20)
    joined_date = models.DateField(auto_now_add=True)
    photo = models.URLField(blank=True)

