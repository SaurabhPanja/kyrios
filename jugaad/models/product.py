from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):

    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    price = models.FloatField(validators=[MinValueValidator(0.0)], blank=False, null=False)

    # education = 
    # institution =
    #relation with other tables 
    # user = 
    # media = 
    # address =


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product'
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'    