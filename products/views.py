# products/views.py
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .models import Product
from .serializers import ProductSerializer

class ProductPagination(PageNumberPagination):
    page_size = 5  # Number of items per page

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination  # Add pagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]  # Enable filtering and ordering
    search_fields = ['name', 'description']  # Fields to search through
    ordering_fields = ['price', 'created_at']  # Fields you can order by