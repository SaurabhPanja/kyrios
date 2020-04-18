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
    def test_product_created(self):
        product_1 = Product.objects.get(title="Calculus 3")

        self.assertEqual(product_1.price, 1000)

        