from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(['POST'])
def create_payment(request: Request) -> Response:
    pass


@api_view(['GET'])
def get_purchase_details(request: Request) -> Response:
    pass


@api_view(['GET'])
def list_transactions(request: Request) -> Response:
    pass
