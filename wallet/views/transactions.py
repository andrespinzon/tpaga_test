from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def create_payment(request) -> Response:
    pass


@api_view(['GET'])
def get_purchase_details(request) -> Response:
    pass


@api_view(['GET'])
def list_transactions(request):
    pass
