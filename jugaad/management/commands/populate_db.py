from django.core.management.base import BaseCommand, CommandError
from jugaad.models import Product

class Command(BaseCommand):
    def handle(self, *args, **options):
        products = [
        {
            "title": "Calculus 1",
            "description":"""Hello everyone this is book on Calculus 1 """, 
            "price": 100
        },
        {
            "title": "Calculus 2",
            "description":"""Hello everyone this is book on Calculus 1 """, 
            "price": 200
        },
        {
            "title": "Calculus 3",
            "description":"""Hello everyone this is book on Calculus 1 """, 
            "price": 300
        },
        {
            "title": "Design Engineering 1",
            "description":"""Hello everyone this is book on Design Engineering 1 """, 
            "price": 400
        },
        {
            "title": "Design Engineering 2",
            "description":"""Hello everyone this is book on Design Engineering 2 """, 
            "price": 500
        },
        {
            "title": "Design Engineering 3",
            "description":"""Hello everyone this is book on Design Engineering 3 """, 
            "price": 600
        },
        {
            "title": "CPU 1",
            "description":"""Hello everyone this is book on CPU 1 """, 
            "price": 700
        },
        {
            "title": "CPU 2",
            "description":"""Hello everyone this is book on CPU 2 """, 
            "price": 800
        },
        {
            "title": "CPU 3",
            "description":"""Hello everyone this is book on CPU 3 """, 
            "price": 900
        },
        {
            "title": "ECE 1",
            "description":"""Hello everyone this is book on ECE 1 """, 
            "price": 1000
        },
        {
            "title": "ECE 2",
            "description":"""Hello everyone this is book on ECE 2 """, 
            "price": 1100
        },
        {
            "title": "ECE 3",
            "description":"""Hello everyone this is book on ECE 3 """, 
            "price": 1200
        },
        {
            "title": "EEE 1",
            "description":"""Hello everyone this is book on EEE 1 """, 
            "price": 1300
        },
        {
            "title": "EEE 2",
            "description":"""Hello everyone this is book on EEE 2 """, 
            "price": 1400
        },
        {
            "title": "EEE 3",
            "description":"""Hello everyone this is book on EEE 3 """, 
            "price": 1500
        },
        ]

        for product in products:
            Product.objects.create(
                title = product["title"],
                description = product["description"],
                price = product["price"]
            )