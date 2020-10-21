from typing import Set, Dict

from rest_framework.exceptions import APIException


class TransactionsService:
    data: Dict = None

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

    def create_payment_from_view(self, data):
        self.data = data

        fields = {'cost', 'purchase_detail_url', ''}
