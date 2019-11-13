from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    )

from products.models import Category, Product
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin

from .serializers import (
    ProductListSerializer, 
    ProductDetailSerializer,
    ProductUpdateCreateSerializer,
    CategoryListSerializer,
    CategoryDetailSerializer,
    )


class CategoryListAPIView(ListAPIView):
    serializer_class = CategoryListSerializer
    
    def get_queryset(self):
        return Category.objects.filter(parent_category__isnull=True)

class CategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer 
    lookup_field = 'slug'

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


    
class ProductDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer 
    lookup_field = 'slug'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateCreateSerializer

class ProductUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateCreateSerializer
    lookup_field = 'slug'

class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'

