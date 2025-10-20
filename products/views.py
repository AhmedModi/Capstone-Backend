from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as django_filters
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Product
from .serializers import ProductSerializer

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    
    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'category']

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all().select_related("category", "owner")
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]  # <-- open to everyone temporarily for testing
    filterset_class = ProductFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["name", "description"]
    ordering_fields = ["price", "name", "created_at"]

    @swagger_auto_schema(
        operation_summary="List products",
        operation_description="List products; supports search, filter, ordering, and pagination.",
        manual_parameters=[
            openapi.Parameter('search', openapi.IN_QUERY, description="Search in name and description", type=openapi.TYPE_STRING),
            openapi.Parameter('min_price', openapi.IN_QUERY, description="Minimum price filter", type=openapi.TYPE_NUMBER),
            openapi.Parameter('max_price', openapi.IN_QUERY, description="Maximum price filter", type=openapi.TYPE_NUMBER),
            openapi.Parameter('category', openapi.IN_QUERY, description="Category name filter", type=openapi.TYPE_STRING),
            openapi.Parameter('ordering', openapi.IN_QUERY, description="Order by field (price, name, created_at)", type=openapi.TYPE_STRING),
        ],
        responses={200: ProductSerializer(many=True)},
        tags=["Products"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create product",
        operation_description="Create a new product",
        request_body=ProductSerializer,
        responses={201: ProductSerializer()},
        tags=["Products"]
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # for test, owner can be None
        serializer.save(owner=None)
        return Response(serializer.data, status=201)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all().select_related("category", "owner")
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]  # <-- open to everyone temporarily for testing

    @swagger_auto_schema(
        operation_summary="Retrieve product",
        operation_description="Get a specific product by ID",
        responses={200: ProductSerializer()},
        tags=["Products"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update product",
        operation_description="Update a specific product by ID",
        request_body=ProductSerializer,
        responses={200: ProductSerializer()},
        tags=["Products"]
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update product",
        operation_description="Partially update a specific product by ID",
        request_body=ProductSerializer,
        responses={200: ProductSerializer()},
        tags=["Products"]
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete product",
        operation_description="Delete a specific product by ID",
        responses={204: "No content"},
        tags=["Products"]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    # Optional: skip permission checks for test
    def check_object_permissions(self, request, obj):
        pass
