from django.db import models



class Image(models.Model):
    im  = models.ImageField()
    im2 = models.ImageField()
    im3 = models.ImageField()


