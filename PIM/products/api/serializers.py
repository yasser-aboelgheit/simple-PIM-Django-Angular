from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    StringRelatedField,
    ManyRelatedField
    )

from products.models import Category, Product

category_detail_url = HyperlinkedIdentityField(
        view_name='category_detail',
        lookup_field='slug'
        )

class CategoryListSerializer(ModelSerializer):
    subcategories = SerializerMethodField(
        read_only=True)
    url = category_detail_url
    class Meta:
        model = Category
        fields = ['id','name','slug','url','subcategories']
    
    def get_subcategories(self, obj):
        serializer = CategoryListSerializer(
            instance=obj.subcategories.all(),
            many=True,
            context=self.context
        )
        return serializer.data


class CategoryDetailSerializer(ModelSerializer):
    product_category = SerializerMethodField(
        read_only=True)
    class Meta:
        model = Category
        fields = '__all__'
    
    def get_product_category(self,obj):
        serializer = ProductListSerializer(
            instance=obj.product_category.all(),
            many=True,
            context=self.context
        )
        return serializer.data


class CategoryUpdateCreateSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


product_detail_url = HyperlinkedIdentityField(
        view_name='detail',
        lookup_field='slug'
        )

class ProductListSerializer(ModelSerializer):
    category = StringRelatedField(many=True)
    url =product_detail_url
    class Meta:
        model = Product
        fields = '__all__'

class ProductDetailSerializer(ModelSerializer):
    url =product_detail_url
    class Meta:
        model = Product
        fields = '__all__'

class ProductUpdateCreateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "product_code", 
            "name",
            "price",
            "quantity",
            "category", 
        ]

