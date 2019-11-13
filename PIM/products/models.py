from django.db import models
from autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField(max_length=100)    
    slug = AutoSlugField(populate_from='name',unique=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE,blank=True, null=True, related_name='subcategories')

    def __str__(self):
        return self.name


class Product(models.Model):
    product_code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name',unique=True)
    price = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, blank=True, related_name='product_category')

    def __str__(self):
        return self.name
