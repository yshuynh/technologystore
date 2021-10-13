from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from app.models import Category, Product
from app.serializers import CategoryFullSerializer, ProductSerializer, CategorySerializer


class CategoryListAPI(generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *arg, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class ProductListAPI(generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

    def get(self, request, *arg, **kwargs):
        page = self.paginate_queryset(self.get_queryset())
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)