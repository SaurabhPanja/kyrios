from django.test import TestCase, Client
from jugaad.models import Product
from rest_framework import status
from django.urls import reverse
from jugaad.serializers import ProductSerializer

client = Client()

# Create your tests here.

class ProductModelTest(TestCase):
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

class RestApiProductTest(TestCase):
    def setUp(self):
        Product.objects.create(
            title="Calculus 3",
            description="""Hello everyone this is a book on calculus """,
            price= 1000
        )
        Product.objects.create(
            title= "Elements of Mechanical Engineering",
            price= 500
        )      
        Product.objects.create(
            title= "Elements of Electrical Engineering",
            price= 750
        )    

    def test_all_products(self):
        response = client.get('/products/')

        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_product(self):
        
        product_1 = Product.objects.first()
        response_1 = client.get('/products/{}/'.format(product_1.id))

        serializer_1 = ProductSerializer(product_1)


        self.assertEqual(response_1.data, serializer_1.data)
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)