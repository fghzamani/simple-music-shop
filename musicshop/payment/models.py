from django.db import models
from user.models import Customer 
from product.models import Track

# Create your models here.
class Invoice(models.Model):
    customer = models.ForeignKey(Customer,on_delete = models.DO_NOTHING , related_name='invoices')
    invoice_date = models.DateTimeField()
    billing_address = models.CharField(max_length=70,blank=True,null=True)
    billing_city = models.CharField(max_length=40,blank=True,null=True)
    billing_state = models.CharField(max_length=40,blank=True,null=True)
    billing_country = models.CharField(max_length=40,blank=True,null=True)
    billing_postal_code = models.CharField(max_length=10,blank=True,null=True)
    total = models.BigIntegerField()



class Invoiceline(models.Model):
    invoice = models.ForeignKey(Invoice,on_delete=models.PROTECT)
    track = models.ForeignKey(Track, on_delete =models.DO_NOTHING)
    unit_price = models.IntegerField()
    quantity =models.IntegerField(default=1)