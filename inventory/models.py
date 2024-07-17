from django.db import models

class Item(models.Model):
    sku = models.CharField(max_length=10, unique=True)
    upc = models.CharField(max_length=14, unique=True)
    description = models.TextField()
    quantity_on_hand = models.IntegerField()
    quantity_on_order = models.IntegerField()
    order_point = models.IntegerField()
    date_of_last_purchase = models.DateField()
    retail_price = models.DecimalField(max_digits=8, decimal_places=2)
    replacement_cost = models.DecimalField(max_digits=8, decimal_places=2)
    current_month_sales = models.IntegerField()
    previous_12_month_sales = models.IntegerField()

    def __str__(self):
        return self.sku


