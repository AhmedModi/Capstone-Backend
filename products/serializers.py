from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        source="category", 
        queryset=Category.objects.all(), 
        write_only=True, 
        required=False, 
        allow_null=True,
        help_text="ID of the category for this product"
    )
    name = serializers.CharField(
        max_length=255,
        help_text="Name of the product"
    )
    description = serializers.CharField(
        allow_blank=True,
        help_text="Description of the product"
    )
    price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Price of the product"
    )
    stock = serializers.IntegerField(
        default=0,
        help_text="Stock quantity of the product"
    )
    image_url = serializers.URLField(
        allow_blank=True,
        required=False,
        help_text="URL of the product image"
    )

    class Meta:
        model = Product
        fields = [
            "id", "name", "slug", "description", "price", "stock",
            "category", "category_id", "image_url", "created_at", "updated_at", "owner"
        ]
        read_only_fields = ["id", "slug", "created_at", "updated_at", "owner"]

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be non-negative.")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock must be non-negative.")
        return value

    def create(self, validated_data):
        # owner set in view
        return super().create(validated_data)
