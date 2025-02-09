from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(max_length=200,blank=True)
    category_image = models.ImageField(upload_to = 'photos/categories',blank=True)


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def get_url(self):
        return reverse('products_by_category',args=[self.slug])  #products_by_category refer from urls.py

    def __str__(self):
        return self.category_name