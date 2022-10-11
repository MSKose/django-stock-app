from rest_framework import serializers
from .models import (
    Category,
    Brand,
    Product,
    Firm,
    Transaction
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'name'
        )


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField(write_only=True)
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'category_id',
            'brand',
            'brand_id',
            'stock'
        )

        read_only_fields = ('stock',)  # since we don't want to create stock field in POST. Rather, we want to define stock on trasaction part


# class CategoryProductsSerializer(serializers.ModelSerializer):
#     products = ProductSerializer(many=True)

#     class Meta:
#         model = Category
#         fields = (
#             'name',
#             'products'
#         )


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = (
            'id',
            'name',
            'phone',
            'address'
        )


class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField() # we only have StringRelatedField for user one since we'll determine the user in our views using the perform_create() method
    firm = serializers.StringRelatedField()
    firm_id = serializers.IntegerField()
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()

    class Meta:
        model = Transaction
        fields = (
            'id',
            'user',
            'firm',
            'firm_id',
            'transaction',
            'product',
            'product_id',
            'quantity',
            'price',
            'price_total'
        )

        read_only_fields = ('price_total',)


    '''
    we have to validate if the OUT transaction amoount is less than or equal to 
    stock total amount. Therfore, we have to override the validate method
    '''
    def validate(self, data):
        if data.get('transaction') == 0: # if transaction is OUT
            product = Product.objects.get(id=data.get('product_id'))
            if data.get('quantity') > product.stock:
                raise serializers.ValidationError(
                    f"You don't have enough stock. Current stock is {product.stock}"
                )
        return data