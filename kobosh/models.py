from django.db import models
from django.urls import reverse
# Create your models here.


from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

from django.core.exceptions import ValidationError

from decimal import Decimal

from django.contrib.humanize.templatetags.humanize import intcomma

class CommaSeparatedIntegerField(models.DecimalField):
    def formated_price(self):
        return "{:,.2f}".format(self.new_price)

class Category(models.Model):

    name = models.CharField(max_length=200)

    image = models.URLField(max_length=200)

    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=["name"]),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('kobosh:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.URLField(max_length=200)

    image1 = models.URLField(max_length=200)

    image2 = models.URLField(max_length=200)
                              
    description = models.TextField(blank=True, max_length=250)
    old_price = CommaSeparatedIntegerField(max_digits=10, decimal_places=0, null=True)
    new_price = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    def formatted_price(self):
        return intcomma(self.new_price)
    
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('kobosh:product_detail',
            args=[self.id, self.slug])



