from rest_framework.serializers import ModelSerializer
from wallet.models import Order


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('original_id', 'cost', 'items', 'description', 'tpaga_transaction')
