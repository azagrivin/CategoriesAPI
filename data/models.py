from django.db import models


class Category(models.Model):
    name = models.TextField(verbose_name='Name')
    childrens = models.ManyToManyField('Category', null=True)
