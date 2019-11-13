from django.urls import path
from django.contrib import admin

from .views import (
    ProductListAPIView,
    ProductDetailAPIView,
    ProductCreateAPIView,
    ProductUpdateAPIView,
    ProductDeleteAPIView,
    CategoryListAPIView,
    CategoryDetailAPIView,
    CategoryCreateAPIView,
    )

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product_list'),
    path('categories', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/create', CategoryCreateAPIView.as_view(), name='create_category'),
    path('categories/<slug:slug>', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('create', ProductCreateAPIView.as_view(), name='create'),
    path('<slug:slug>', ProductDetailAPIView.as_view(), name='detail'),
    path('<slug:slug>/update', ProductUpdateAPIView.as_view(), name='update'),
    path('<slug:slug>/delete', ProductDeleteAPIView.as_view(), name='delete'),
    
]
