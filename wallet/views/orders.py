from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from wallet.services import OrdersService


class OrdersView(APIView):

    def post(self, request: Request) -> Response:
        service = OrdersService()
        data = service.create_order_from_view(data=request.data)
        return Response(data=data, status=HTTP_201_CREATED)
