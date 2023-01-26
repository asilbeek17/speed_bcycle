from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=55)
    image = models.ImageField()
    text = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('gallery', args=[str(self.pk)])
