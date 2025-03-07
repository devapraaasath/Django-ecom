from django.db import models
import datetime
import os
from django.contrib.auth.models import User

# Create your models here.

# Function to generate a unique filename for uploaded files
def getfilename(request, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = "%s%s" % (now_time, filename)
    return os.path.join('uploads/', new_filename)

# Category model to store product categories
class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getfilename, null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-default, 1-hidden")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Product model to store product details
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=150, null=False, blank=False)
    vendor = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(upload_to=getfilename, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)  # Updated to FloatField
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-default, 1-hidden")
    trending = models.BooleanField(default=False, help_text="0-default, 1-trending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Cart model to store user's cart items
class Cart(models.Model):
    # ForeignKey to link each cart to a specific user
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # When a User is deleted, all related Cart instances will also be deleted
    Product= models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)



    @property
    def total_cost(self):
        return self.product_qty*self.Product.selling_price

class fav(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)