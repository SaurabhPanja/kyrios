from django.shortcuts import render
from jugaad.models import Product, Institution
from rest_framework import viewsets
from rest_framework import permissions
from jugaad.serializers import ProductSerializer, InstitutionSerializer
from rest_framework.renderers import JSONRenderer
class ProductViewSet(viewsets.ModelViewSet):
    
    renderer_classes = [JSONRenderer]

    queryset = Product.objects.get_queryset().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class InstitutionViewSet(viewsets.ModelViewSet):
    
    renderer_classes = [JSONRenderer]

    queryset = Institution.objects.get_queryset().order_by('id')
    serializer_class = InstitutionSerializer
    
