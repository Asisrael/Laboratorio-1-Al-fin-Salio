from django.db import models
from ..vehiculo.models import Vehiculo
from ..cliente.models import Customer
from django.db.models.signals import pre_save, post_save, post_delete


class Invoice(models.Model):
    """Model definition for Invoice."""

    # TODO: return customer name from order

    PAYMENT_CHOICES = [
        ("efe", "efectivo"),
        ("tar", "tarjeta"),
        ("cu", "cupon"),
    ]
    invoice_number = models.CharField(max_length=12)
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    order = models.OneToOneField("Order", on_delete=models.CASCADE)
    payment = models.CharField(max_length=2, choices=PAYMENT_CHOICES)

    def __str__(self):
        return str(self.order.id)
    
    def total(self):
        return self.order.total

class Order(models.Model):
    """Customer orders and state management."""

    # TODO: delivery_type: To eat here or carry out

    STATUS_CHOICES = [
        ("Adentro", "Adentro"),
        ("Afuera", "Afuera"),
    ]
    date = models.DateTimeField(auto_now_add=True)
    vehiculo = models.ManyToManyField(Vehiculo, through="OrderDetail")
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default="re")
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class OrderDetail(models.Model):
    """Order detail as quantity of each product and price."""

    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.Vehiculo.plate





