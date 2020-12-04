from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from jugaad.models import Product

#negative price should not be saved in the database
@receiver(pre_save, sender=Product)
def validate_product_price(instance, sender, **kwargs):
    if instance.price < 0.0:
        instance.price = 0.0

