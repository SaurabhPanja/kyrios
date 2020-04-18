from django.test import TestCase
from jugaad.models import Product

# Create your tests here.

class ProductTest(TestCase):
    def setUp(self):
        Product.objects.create(
            title="Calculus 3",
            description="""Hello everyone this is a book on calculus """,
            price= 1000
        )
        Product.objects.create(
            title= "Elements of Mechanical Engineering",
            price= -10
        )

    #testing model        
    def test_product_created(self):
        product = Product.objects.get(title="Calculus 3")

        self.assertEqual(product.price, 1000)
    
    def test_negative_price(self):
        product = Product.objects.get(title="Elements of Mechanical Engineering")
        
        self.assertEqual(product.price, 0)

