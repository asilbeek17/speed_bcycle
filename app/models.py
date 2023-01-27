from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=155)
    image = models.ImageField()
    text = models.TextField()
    price = models.FloatField()
    quantitiy = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.pk)])


class Contact(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    message = models.TextField()

