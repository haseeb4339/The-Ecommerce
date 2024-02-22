from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank = True)
    cat_img = models.ImageField(upload_to='photos/categories')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        # db_table = 'category'  # Specify the desired table name here

    def __str__(self):
        return self.category_name
