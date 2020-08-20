from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Out Door','Out Door')
    )
    name = models.CharField(max_length=150, null=True)
    price = models.FloatField(null=True)
    category  = models.CharField(max_length=200,choices=CATEGORY,null=True)
    description = models.CharField(max_length=150, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null = True)
class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered')
    )

    customer = models.ForeignKey(Customer, null=True,on_delete = models.SET_NULL,related_name='Order')
    product = models.ForeignKey(Customer, null=True, on_delete = models.SET_NULL,related_name='products')
    date_created = models.DateTimeField(auto_now_add=True, null = True)
    status = models.CharField(max_length=200,choices=STATUS,null=True)

class Tag(models.Model):
    name = models.CharField(max_length=150, null=True)
    def __str__(self):
        return self.name