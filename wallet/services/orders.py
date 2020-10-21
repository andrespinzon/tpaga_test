from typing import Set, Dict
from uuid import uuid4

from rest_framework.exceptions import APIException
from django.core.exceptions import ValidationError
from django.db.transaction import atomic as atomic_transaction

from wallet.models import Order
from wallet.serializers import OrderSerializer


class OrdersService:
    data: Dict = None
    order: Order

    def __validate_allowed_fields(self, allowed_fields: Set, model_name: str):
        if not self.data or not isinstance(self.data, dict):
            raise APIException(detail='Invalid data.')
        for key in self.data:
            if key not in allowed_fields:
                raise APIException(detail=f'Invalid field "{key}" for {model_name} model.')

    def __validate_required_fields(self, required_fields: Set):
        for key in required_fields:
            if key not in self.data:
                raise APIException(detail=f'Key {key} is required.')

    def __add_additional_data(self):
        original_token = f'{self.order.id}{uuid4()}'.encode()
        self.order.original_id = original_token
        self.order.idempotency_token = original_token
        self.order.save()

    def create_order_from_view(self, data):
        self.data = data

        fields = {'cost', 'terminal_id', 'description', 'items'}

        self.__validate_allowed_fields(allowed_fields=fields, model_name='Order')
        self.__validate_required_fields(required_fields=fields)

        try:
            with atomic_transaction():
                self.order: Order = Order.objects.create(**self.data)
                self.__add_additional_data()



        except ValidationError as error:
            raise APIException(detail=error.message[0])

        return OrderSerializer(instance=self.order).data

