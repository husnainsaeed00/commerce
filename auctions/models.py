from django.contrib.auth.models import AbstractUser
from django.db import models

class Category(models.Model):
    categoryName = models.CharField(max_length=30)

    def __str__(self):
        return self.categoryName


class User(AbstractUser):
    pass
class Listing(models.Model):
    title= models.CharField(max_length=30)
    description=models.CharField(max_length=300)
    imageurl = models.ImageField(upload_to='listing_images/', null=True, blank=True)
    price=models.FloatField()
    isActive= models.BooleanField(default=True)
    owner=models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True,related_name="user")
    category=models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True,related_name="category")
    def __str__(self):
        return self.title