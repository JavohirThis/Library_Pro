from django.db import models

# Create your models here.

from django.db import models

from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('a','Admin'),
        ('A','Author'),
        ('b','Book')
    )
    roles = models.CharField(max_length=1,choices=ROLE_CHOICES)

# Create your models here.

class AuthorModel(models.Model):
    name = models.CharField(max_length=50, default='')
    fname = models.CharField(max_length=50, default='')
    date_of_birth = models.DateField(default=datetime.now)
    country=models.CharField(max_length=25,default='')
    class Meta:
        db_table = 'author'
class BookCategoryModel(models.Model):
    name = models.CharField(max_length=50, default='')
class BookModel(models.Model):
    category =models.ForeignKey(BookCategoryModel,on_delete=models.SET_NULL,null=True)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    page = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None, null=True)
    year=models.DateTimeField(default=datetime.now)
    info=models.CharField(max_length=200,default='')
    class Meta:
        db_table = 'book'
