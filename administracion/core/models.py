from django.db import models

class Category(models.Model):

    class Meta:
        db_table = "category"

    name = models.CharField(max_length=150, blank=False, null=False, unique=True)

class Product(models.Model):
    
    class Meta:
        db_table = "product"

    category = models.ForeignKey(to= Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=250, blank=False, null=False)
    quantity = models.IntegerField()
    um = models.CharField(max_length=50)
    purchase_price = models.DecimalField(decimal_places=2, max_digits=18)
    sale_price = models.DecimalField(decimal_places=2, max_digits=18)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
