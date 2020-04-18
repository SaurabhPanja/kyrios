from django.test import TestCase, Client
from jugaad.models import Product
from rest_framework import status
from django.urls import reverse
from jugaad.serializers import ProductSerializer
import json


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

    def test_get_product(self):
        
        product_1 = Product.objects.first()
        response_1 = client.get('/products/{}/'.format(product_1.id))

        serializer_1 = ProductSerializer(product_1)


        self.assertEqual(response_1.data, serializer_1.data)
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)

    def test_create_valid_product(self):
        self.valid_data = {
            'title': "Mechatronics",
            'description': "A cool book on mechatronics",
            'price': 999.0
        }
        response = client.post('/products/',\
            data=json.dumps(self.valid_data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_product(self):
        self.invalid_data = {
            'title': "",
            'description': "A cool book on mechatronics",
            'price': ''
        }
        response = client.post('/products/',\
            data=json.dumps(self.invalid_data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)        
    
    def test_valid_update_product(self):

        self.valid_data = {
            'title': "Mechatronics",
            'description': "A cool book on mechatronics",
            'price': 999.0
        }

        product_id = Product.objects.first().id

        response = client.put('/products/{}/'.format(product_id), \
            data=json.dumps(self.valid_data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_valid_delete_product(self):
        product_id = Product.objects.last().id

        response = client.delete('/products/{}/'.format(product_id))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_product(self):
        invalid_product_id = 9999
        response = client.delete('/products/999/'.format(invalid_product_id))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
