from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Lead(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    interested_products = models.ManyToManyField(Product, related_name='leads', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name